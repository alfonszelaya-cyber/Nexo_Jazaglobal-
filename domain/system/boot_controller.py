# ============================================================
# boot_controller.py
# NEXO / ZYRA — CONTROLADOR DE ARRANQUE CANÓNICO
# CORE | SAFE | AUDITABLE | 10+ AÑOS
# ============================================================

import os
from datetime import datetime

from domain.security.safe_mode import (
    activate_safe_mode,
    activate_degraded_mode,
    restore_normal_mode,
    MODE_SAFE,
    MODE_DEGRADED,
    MODE_NORMAL,
    get_mode_snapshot
)
from domain.security.integrity_checker import run_boot_integrity, BOOT_OK, BOOT_SAFE, BOOT_HALT
from domai.sytem.shutdown import record_shutdown

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# ============================================================
# BOOT CONTROLLER
# ============================================================

class BootController:
    """
    Controlador principal de arranque del CORE ZYRA/NEXO
    - Valida integridad de archivos críticos
    - Decide modo de arranque: NORMAL / SAFE / DEGRADED
    - Registra eventos de inicio/apagado
    """

    def __init__(self, base_dir=None):
        self.base_dir = base_dir or BASE_DIR
        self.boot_status = None
        self.integrity_report = None
        self.timestamp = datetime.utcnow().isoformat()

    def start_boot(self):
        """
        Ejecuta secuencia de arranque:
        1. Verifica integridad
        2. Decide estado del CORE
        3. Devuelve snapshot del boot
        """
        self.integrity_report = run_boot_integrity(self.base_dir)
        boot_code = self.integrity_report.get("boot", BOOT_HALT)

        if boot_code == BOOT_OK:
            restore_normal_mode(activated_by="BOOT_CONTROLLER")
            self.boot_status = MODE_NORMAL
        elif boot_code == BOOT_SAFE:
            activate_safe_mode(reason="BOOT_INTEGRITY_FAIL", activated_by="BOOT_CONTROLLER")
            self.boot_status = MODE_SAFE
        else:
            activate_degraded_mode(reason="BOOT_CRITICAL_FAIL", activated_by="BOOT_CONTROLLER")
            self.boot_status = MODE_DEGRADED
            record_shutdown(reason="BOOT_CRITICAL_HALT", initiated_by="BOOT_CONTROLLER")

        return self.boot_snapshot()

    def boot_snapshot(self):
        """ Devuelve estado completo del arranque, integridad y modos """
        return {
            "timestamp": self.timestamp,
            "boot_status": self.boot_status,
            "mode_snapshot": get_mode_snapshot(),
            "integrity_report": self.integrity_report
        }

    def is_normal(self):
        return self.boot_status == MODE_NORMAL

    def is_safe(self):
        return self.boot_status == MODE_SAFE

    def is_degraded(self):
        return self.boot_status == MODE_DEGRADED
