# module_metrics.py
# NEXO / ZYRA — LOGÍSTICA ASIA
# MÉTRICAS BÁSICAS DEL MÓDULO
# PASIVO | EVENT-DRIVEN

from datetime import datetime, timezone

MODULE_METRICS = {
    "events_processed": 0,
    "alerts_triggered": 0,
    "last_event_ts": None,
    "uptime_start": datetime.now(timezone.utc).isoformat()
}

def record_event(event_type: str):
    MODULE_METRICS["events_processed"] += 1
    MODULE_METRICS["last_event_ts"] = datetime.now(timezone.utc).isoformat()
    if event_type == "LOGISTICS_ALERT":
        MODULE_METRICS["alerts_triggered"] += 1