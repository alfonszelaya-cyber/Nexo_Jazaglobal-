from domain.finance.ledger import Ledger
from infrastructure.events.zyra_bus import ZyraBus
from infrastructure.logging.zyra_logger import ZyraLogger


class CreateLedgerEntryUseCase:

    def __init__(self, ledger: Ledger):
        self.ledger = ledger

    def execute(self, entry_data: dict):
        entry = self.ledger.create_entry(entry_data)

        ZyraLogger.info("Ledger entry created")

        ZyraBus.emit("ledger_entry_created", entry)

        return entry
