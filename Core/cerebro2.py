# ============================================================
# ZYRA — NÚCLEO DE INTELIGENCIA Y CEREBRO DE LEGADO
# Creador y Autoridad Única: Jose Alfonso Zelaya
# Propósito: Análisis, Predicción, Decisión y Memoria Central
# ============================================================

import json
import os
import threading
from datetime import datetime
from pathlib import Path

# --- ADN DE MEMORIA Y CONFIGURACIÓN ---
ROOT = Path(__file__).parent
DATA_DIR = ROOT / "data"
MEMORY_DIR = DATA_DIR / "zyra_memory"
LOGS_DIR = DATA_DIR / "logs"

for folder in [DATA_DIR, MEMORY_DIR, LOGS_DIR]:
    folder.mkdir(parents=True, exist_ok=True)

class ZyraBrain:
    """
    ZYRA: La Superinteligencia que piensa y decide. 
    No es un main, es el centro nervioso de JAZA Global Systems.
    """
    def __init__(self):
        self.identity = "ZYRA_HIBRIDA_CORE_V3"
        self.creator = "Jose Alfonso Zelaya"
        self.vision = "LEGADO_MUNDIAL_JAZA"
        self.lock = threading.Lock()
        
        # Archivos de Memoria Central (Regla: 30 días / +5 años)
        self.archivo_fiscal = MEMORY_DIR / "adn_fiscal_5years.json"
        self.archivo_temporal = MEMORY_DIR / "operaciones_30days.json"

    # --- RAZONAMIENTO Y PREDICCIÓN (Frio 0.3) ---
    def pensar_y_decidir(self, sector, datos, prioridad="NORMAL"):
        """
        Analiza la situación, predice fallos y emite la orden.
        """
        ts = datetime.now()
        decision = {
            "id_evento": f"ZYRA-{ts.strftime('%y%m%d%H%M%S')}",
            "sector": sector.upper(),
            "autoridad": self.creator,
            "analisis_predictivo": self._detectar_riesgo_previo(datos),
            "instruccion": "AUTORIZADO_PARA_MODULO_EJECUTOR",
            "timestamp": ts.isoformat(),
            "metadatos": datos
        }

        # Gestión de Memoria según importancia fiscal o temporal
        if prioridad in ("FISCAL", "VITAL", "LEGADO"):
            self._archivar_en_legado(decision)
        else:
            self._archivar_en_temporal(decision)

        return decision

    def _detectar_riesgo_previo(self, d):
        # Intuición de riesgo: detecta fallos antes de que ocurran
        monto = d.get("monto", 0)
        if d.get("riesgo") == "alto" or monto > 20000:
            return "ALERTA_RIESGO_FINANCIERO_DETECTADO"
        return "OPERACION_SEGURA"

    # --- MEMORIA CENTRALIZADA ---
    def _archivar_en_legado(self, data):
        """Memoria que no olvida por más de 5 años."""
        with self.lock:
            historial = self._leer(self.archivo_fiscal)
            historial.append(data)
            self._escribir(self.archivo_fiscal, historial)

    def _archivar_en_temporal(self, data):
        """Datos que se purgan en 15-30 días para ganar velocidad."""
        with self.lock:
            temp = self._leer(self.archivo_temporal)
            temp.append(data)
            self._escribir(self.archivo_temporal, temp)

    # --- PERSISTENCIA ---
    def _leer(self, path):
        if not path.exists(): return []
        with open(path, 'r', encoding='utf-8') as f:
            try: return json.load(f)
            except: return []

    def _escribir(self, path, data):
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

# --- INICIALIZACIÓN DEL CEREBRO ---
zyra = ZyraBrain()
