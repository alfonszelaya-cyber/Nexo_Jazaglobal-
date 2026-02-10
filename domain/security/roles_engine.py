# ============================================================
# roles_engine.py
# NEXO / ZYRA — MOTOR DE ROLES & PERMISOS GLOBALES
# Constitución Digital | Inmutable | Multiapp
# ============================================================

import json

# ============================================================
# 1. DEFINICIÓN MAESTRA DE ROLES (LA CONSTITUCIÓN)
# ============================================================

ROLES_GLOBALES = {
    # --------------------------------------------------------
    # NIVEL 0: GOBIERNO DEL SISTEMA (SUPREMO)
    # --------------------------------------------------------
    "SUPER_ROOT": {
        "nivel": 0,
        "descripcion": "Control total del ecosistema NEXO / ZYRA",
        "ambito": "GLOBAL",
        "apps_acceso": ["NEXO", "SEMILLA", "AXIS", "AGROP", "NUEVO_TRABAJO"],
        "permisos_clave": ["TODO", "ACCESO_TOTAL_DB", "APAGADO_EMERGENCIA"]
    },

    "GOBIERNO_AUDITOR": {
        "nivel": 1,
        "descripcion": "Entidades estatales, Hacienda, Ministerios",
        "ambito": "GLOBAL",
        "apps_acceso": ["NEXO", "AGROP"],
        "permisos_clave": ["VER_DATOS_AGREGADOS", "FISCALIZAR", "AUDITAR_IMPUESTOS"]
    },

    # --------------------------------------------------------
    # NIVEL 1: EMPRESARIAL (NEXO)
    # --------------------------------------------------------
    "PROPIETARIO_EMPRESA": {
        "nivel": 10,
        "descripcion": "Dueño legal de empresa registrada",
        "ambito": "EMPRESA",
        "apps_acceso": ["NEXO"],
        "permisos_clave": ["VER_TODO_EMPRESA", "AUTORIZAR_PAGOS", "CONFIGURACION_MASTER"]
    },

    "CONTADOR_CERTIFICADO": {
        "nivel": 11,
        "descripcion": "Contador responsable ante Hacienda",
        "ambito": "EMPRESA",
        "apps_acceso": ["NEXO"],
        "permisos_clave": ["VER_FINANZAS", "DECLARAR_IMPUESTOS", "FIRMAR_LIBROS"]
    },

    "OPERADOR_VENTAS": {
        "nivel": 12,
        "descripcion": "Punto de venta y atención",
        "ambito": "EMPRESA",
        "apps_acceso": ["NEXO"],
        "permisos_clave": ["FACTURAR", "VER_INVENTARIO_LOCAL", "REGISTRAR_CLIENTE"]
    },

    # --------------------------------------------------------
    # NIVEL 2: EDUCACIÓN (SEMILLA)
    # --------------------------------------------------------
    "DIRECTOR_ACADEMICO": {
        "nivel": 20,
        "descripcion": "Director de institución educativa",
        "ambito": "EDUCATIVO",
        "apps_acceso": ["SEMILLA", "AXIS"],
        "permisos_clave": ["GESTION_ALUMNOS", "ALERTAS_SEGURIDAD", "VER_CALIFICACIONES"]
    },

    "ESTUDIANTE": {
        "nivel": 22,
        "descripcion": "Usuario en aprendizaje activo",
        "ambito": "PERSONAL",
        "apps_acceso": ["SEMILLA"],
        "permisos_clave": ["VER_CONTENIDO", "TOMAR_EXAMEN", "VER_PROGRESO"]
    },

    # --------------------------------------------------------
    # NIVEL 3: SALUD & SEGURIDAD (AXIS)
    # --------------------------------------------------------
    "MEDICO_AXIS": {
        "nivel": 30,
        "descripcion": "Profesional de la salud certificado",
        "ambito": "PROFESIONAL",
        "apps_acceso": ["AXIS"],
        "permisos_clave": ["VER_EXPEDIENTE_CLINICO", "RECETAR", "EMITIR_DIAGNOSTICO"]
    },

    # --------------------------------------------------------
    # NIVEL 4: SECTOR PRIMARIO (AGROP)
    # --------------------------------------------------------
    "PRODUCTOR_AGRO": {
        "nivel": 40,
        "descripcion": "Productor agrícola o ganadero",
        "ambito": "PRODUCTIVO",
        "apps_acceso": ["AGROP", "NEXO"],
        "permisos_clave": ["REGISTRAR_COSECHA", "SOLICITAR_CREDITO", "TRAZABILIDAD"]
    },

    # --------------------------------------------------------
    # NIVEL 5: CIUDADANÍA (BASE)
    # --------------------------------------------------------
    "CIUDADANO_VERIFICADO": {
        "nivel": 99,
        "descripcion": "Usuario base con identidad validada",
        "ambito": "PERSONAL",
        "apps_acceso": ["NEXO", "NUEVO_TRABAJO"],
        "permisos_clave": ["COMPRAR", "POSTULAR_EMPLEO", "PAGAR_SERVICIOS"]
    }
}

# ============================================================
# 2. MOTOR DE VERIFICACIÓN (LA LÓGICA)
# ============================================================

class ZyraPermissionSystem:

    @staticmethod
    def get_role_info(role_key):
        """Devuelve la metadata completa de un rol"""
        return ROLES_GLOBALES.get(role_key)

    @staticmethod
    def can_access_app(role_key, app_name):
        """Verifica si un rol puede entrar a una App específica"""
        role = ROLES_GLOBALES.get(role_key)
        if not role:
            return False

        # SUPER_ROOT entra a todo
        if role_key == "SUPER_ROOT":
            return True

        return app_name in role.get("apps_acceso", [])

    @staticmethod
    def has_permission(role_key, permission_required):
        """Verifica si un rol tiene un permiso específico"""
        role = ROLES_GLOBALES.get(role_key)
        if not role:
            return False

        # Root lo puede todo
        if "TODO" in role.get("permisos_clave", []):
            return True

        return permission_required in role.get("permisos_clave", [])

    @staticmethod
    def validar_jerarquia(role_emisor, role_objetivo):
        """
        Un usuario no puede modificar a alguien
        de mayor rango (nivel numérico menor = más rango).
        """
        emisor = ROLES_GLOBALES.get(role_emisor)
        objetivo = ROLES_GLOBALES.get(role_objetivo)

        if not emisor or not objetivo:
            return False

        return emisor["nivel"] <= objetivo["nivel"]

# ============================================================
# 3. EJECUCIÓN DE PRUEBA
# ============================================================

if __name__ == "__main__":
    print("--- TEST ROLES ENGINE ZYRA ---")

    rol = "PROPIETARIO_EMPRESA"
    app = "SEMILLA"
    acceso = ZyraPermissionSystem.can_access_app(rol, app)
    print(f"¿{rol} puede acceder a {app}? -> {acceso}")

    rol_conta = "CONTADOR_CERTIFICADO"
    permiso = "DECLARAR_IMPUESTOS"
    puede_declarar = ZyraPermissionSystem.has_permission(rol_conta, permiso)
    print(f"¿{rol_conta} puede {permiso}? -> {puede_declarar}")

    es_jefe = ZyraPermissionSystem.validar_jerarquia("SUPER_ROOT", "GOBIERNO_AUDITOR")
    print(f"¿SUPER_ROOT manda sobre GOBIERNO? -> {es_jefe}")