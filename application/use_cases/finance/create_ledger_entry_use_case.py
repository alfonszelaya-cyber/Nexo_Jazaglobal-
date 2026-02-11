# ============================================================
# CREATE LEDGER ENTRY USE CASE
# Conecta Application → Domain (ledger_record)
# Arquitectura estable y coherente con tu dominio actual
# ============================================================

from domain.finance.ledger import ledger_record


class CreateLedgerEntryUseCase:

    def execute(self, evento: str, estado: str, payload: dict = None, origen: str = "SYSTEM"):
        return ledger_record(
            evento=evento,
            estado=estado,
            payload=payload,
            origen=origen
        )
