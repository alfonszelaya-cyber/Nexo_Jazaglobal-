# ============================================================
# ZYRA / NEXO
# BASE MODEL — ENTERPRISE 3.0
# SQLAlchemy Declarative Base
# ============================================================

from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    """
    Base declarativa global del sistema.
    Todas las tablas ORM deben heredar de aquí.
    """
    pass
