# ============================================================
# core_metrics.py
# Métricas y estadísticas del CORE ZYRA
# ============================================================

import time
import threading

_start_time = time.time()
_event_count = 0
_lock = threading.Lock()

def uptime() -> float:
    """
    Devuelve el tiempo de actividad del CORE en segundos
    """
    return time.time() - _start_time

def inc_event():
    """
    Incrementa el contador de eventos procesados
    """
    global _event_count
    with _lock:
        _event_count += 1

def get_event_count() -> int:
    """
    Devuelve el número total de eventos procesados
    """
    with _lock:
        return _event_count

def metrics() -> dict:
    """
    Devuelve un diccionario con métricas clave del CORE
    """
    return {
        "uptime": uptime(),
        "events": get_event_count()
        
       
    }
    
    # ============================================================
# core_metrics.py
# NEXO / ZYRA — CORE METRICS
# Uptime | Eventos | Boots
# ============================================================

from datetime import datetime

# -------------------------
# ESTADO INTERNO
# -------------------------
_START_TS = datetime.utcnow()
_BOOT_COUNT = 0
_EVENT_COUNT = 0


def _now():
    return datetime.utcnow()


# -------------------------
# MARCADORES
# -------------------------
def mark_boot():
    global _BOOT_COUNT
    _BOOT_COUNT += 1


def mark_event():
    global _EVENT_COUNT
    _EVENT_COUNT += 1


# -------------------------
# MÉTRICAS
# -------------------------
def uptime_seconds():
    delta = _now() - _START_TS
    return int(delta.total_seconds())


def metrics():
    return {
        "uptime_seconds": uptime_seconds(),
        "boot_count": _BOOT_COUNT,
        "event_count": _EVENT_COUNT,
        "started_at": _START_TS.isoformat()
    }


# -------------------------
# RESET CONTROLADO (solo tests)
# -------------------------
def _reset_metrics():
    global _START_TS, _BOOT_COUNT, _EVENT_COUNT
    _START_TS = datetime.utcnow()
    _BOOT_COUNT = 0
    _EVENT_COUNT = 0