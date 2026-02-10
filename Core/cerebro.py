# ======================================================
# ZYRA / NEXO — CEREBRO CENTRAL GLOBAL V3
# Archivo raíz: zyra_main.py
# Autor: Jose Alfonso Zelaya
# ======================================================

import os
import sys
import importlib
import traceback
import json
import datetime
import threading
from pathlib import Path
import requests
import time

# ======================================================
# CONFIGURACIÓN DE CARPETAS
# ======================================================

ROOT = Path(__file__).parent
MODULE_DIR = ROOT / "module"
DATA_DIR = ROOT / "data"
LOGS_DIR = DATA_DIR / "logs"
MEMORY_DIR = DATA_DIR / "zyra_memory"
SHORT_TERM = MEMORY_DIR / "short_term"
LONG_TERM = MEMORY_DIR / "long_term"

for folder in [SHORT_TERM, LONG_TERM, LOGS_DIR]:
    folder.mkdir(parents=True, exist_ok=True)

if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

# ======================================================
# MEMORIA CENTRAL UNIFICADA
# ======================================================

memory_lock = threading.Lock()

class ZyraMemory:
    def __init__(self):
        self.short_term_dir = SHORT_TERM
        self.long_term_dir = LONG_TERM
        self.temporal_file = SHORT_TERM / "operaciones_transitorias.json"
        self.fiscal_file = LONG_TERM / "documentos_fiscales.json"

        for file in [self.temporal_file, self.fiscal_file]:
            if not file.exists():
                with open(file, "w", encoding="utf-8") as f:
                    json.dump([], f, indent=2, ensure_ascii=False)

    def guardar(self, nombre, contenido, largo_plazo=False):
        carpeta = self.long_term_dir if largo_plazo else self.short_term_dir
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        archivo = carpeta / f"{timestamp}_{nombre}.json"

        with memory_lock:
            with open(archivo, "w", encoding="utf-8") as f:
                json.dump(contenido, f, indent=2, ensure_ascii=False)

        return archivo

    def guardar_documento(self, ruta_archivo, tipo="normal"):
        largo_plazo = tipo in ("fiscal", "contrato")
        nombre = Path(ruta_archivo).stem
        contenido = {
            "path": str(ruta_archivo),
            "tipo": tipo,
            "fecha": str(datetime.datetime.now())
        }
        return self.guardar(nombre, contenido, largo_plazo=largo_plazo)

    def limpiar_temporal(self, dias=30):
        now = datetime.datetime.now()
        for archivo in self.short_term_dir.glob("*.json"):
            created = datetime.datetime.fromtimestamp(archivo.stat().st_mtime)
            if (now - created).days > dias:
                archivo.unlink()

    def leer_memoria(self, largo_plazo=False):
        carpeta = self.long_term_dir if largo_plazo else self.short_term_dir
        registros = []

        for archivo in carpeta.glob("*.json"):
            with open(archivo, "r", encoding="utf-8") as f:
                try:
                    registros.append(json.load(f))
                except:
                    continue
        return registros

    def mantenimiento_diario(self, dias_temporal=30):
        self.limpiar_temporal(dias=dias_temporal)

# Instancia global de memoria
zyra_memory = ZyraMemory()

# ======================================================
# NÚCLEO DE INTELIGENCIA ZYRA
# ======================================================

class ZyraBrain:
    def __init__(self):
        self.identity = "ZYRA_SUPERINTELIGENCIA_HIBRIDA"
        self.creator = "Jose Alfonso Zelaya"
        self.vision = "LEGADO_MUNDIAL_JAZA"
        os.makedirs(DATA_DIR, exist_ok=True)

    def procesar_logica_universal(self, sector, datos, prioridad="NORMAL"):
        timestamp = datetime.datetime.now()
        analisis = {
            "id_evento": f"ZYRA-{timestamp.strftime('%y%m%d%H%M%S')}",
            "sector": sector.upper(),
            "vision_legado": True,
            "autoridad_validada": self.creator,
            "prediccion_riesgo": self._analizar_riesgo(datos),
            "flujo_vital": ["NEXO", "AXIS", "SEMILLA"],
            "metadatos": datos
        }

        if prioridad in ("FISCAL", "VITAL", "CONTRATO"):
            self._guardar_legado(analisis)
        else:
            self._guardar_temporal(analisis)

        return analisis

    def _analizar_riesgo(self, datos):
        return "NIVEL_OPTIMO" if not datos.get("error") else "ALERTA_PREDICTIVA"

    def _guardar_legado(self, data):
        zyra_memory.guardar(data.get("id_evento", "legado"), data, largo_plazo=True)

    def _guardar_temporal(self, data):
        zyra_memory.guardar(data.get("id_evento", "temporal"), data, largo_plazo=False)

    def convertir_moneda(self, monto, moneda_origen="USD", moneda_destino="BTC"):
        try:
            url = f"https://api.exchangerate.host/latest?base={moneda_origen}&symbols={moneda_destino}"
            tasa = requests.get(url, timeout=5).json()["rates"][moneda_destino]
            return round(monto * tasa, 8)
        except:
            return monto

# Instancia global del cerebro
zyra = ZyraBrain()

# ======================================================
# APPS FUTURAS
# ======================================================

REGISTERED_APPS = {}

def registrar_app(nombre_app, interface_func):
    REGISTERED_APPS[nombre_app] = interface_func

def ejecutar_app(nombre_app, *args, **kwargs):
    if nombre_app in REGISTERED_APPS:
        return REGISTERED_APPS[nombre_app](*args, **kwargs)
    raise ValueError(f"App {nombre_app} no registrada.")

# ======================================================
# CARGA DE MÓDULOS
# ======================================================

def cargar_modulos():
    OK, FAIL = [], []

    if not MODULE_DIR.exists():
        print("[WARN] Carpeta module no encontrada")
        return OK, FAIL

    print(f"\n=== Escaneando módulos en {MODULE_DIR} ===\n")

    for file in sorted(MODULE_DIR.glob("*.py")):
        if file.name.startswith("__"):
            continue

        module_name = file.stem
        full_import = f"module.{module_name}"

        try:
            importlib.import_module(full_import)
            print(f"[ OK ] {full_import}")
            OK.append(full_import)
        except Exception as e:
            print(f"[FAIL] {full_import}")
            trace = traceback.format_exc(limit=5)
            FAIL.append((full_import, trace))
            zyra_memory.guardar(
                f"error_import_{module_name}",
                {"error": str(e), "traceback": trace},
                largo_plazo=True
            )

    print("\n==============================================")
    print(f"TOTAL OK   : {len(OK)}")
    print(f"TOTAL FAIL : {len(FAIL)}")
    print("==============================================\n")

    return OK, FAIL

# ======================================================
# ACTUALIZACIÓN AUTÓNOMA
# ======================================================

def actualizar_nucleo(url_actualizacion):
    try:
        resp = requests.get(url_actualizacion, timeout=10)
        if resp.status_code == 200:
            archivo = ROOT / "zyra_update.py"
            with open(archivo, "w", encoding="utf-8") as f:
                f.write(resp.text)
            return True, archivo
        return False, None
    except Exception as e:
        return False, str(e)

# ======================================================
# DETECCIÓN DE DOCUMENTOS
# ======================================================

def detectar_documento(tipo, ruta_archivo):
    return zyra_memory.guardar_documento(ruta_archivo, tipo=tipo)

# ======================================================
# MANTENIMIENTO
# ======================================================

def mantenimiento_diario():
    zyra_memory.mantenimiento_diario(dias_temporal=30)

# ======================================================
# EJECUCIÓN PRINCIPAL
# ======================================================

if __name__ == "__main__":
    print("✅ ZYRA / NEXO MAIN SUPER ESTABLE GLOBAL V3 ACTIVO")

    cargar_modulos()

    archivo = detectar_documento("fiscal", "factura_123.pdf")
    print("Documento fiscal guardado:", archivo)

    registrar_app("MiPrimerEmpleo", lambda x: f"Procesando {x}")
    resultado = ejecutar_app("MiPrimerEmpleo", "vacante_001")
    print("Resultado App:", resultado)

    monto = zyra.convertir_moneda(100, "USD", "BTC")
    print("100 USD en BTC:", monto)

    actualizado, info = actualizar_nucleo("https://tuservidor.com/zyra_update.py")
    print("Actualización núcleo:", actualizado, info)

    print("\n🛑 Pausa de 10 segundos para revisión completa...")
    time.sleep(10)