# ============================================================
# ZYRA / NEXO
# DB INIT — ENTERPRISE CORE
# Production Table Bootstrap
# ============================================================

from infrastructure.database.db_session import engine, Base


def init_database() -> None:
    """
    Initialize all database tables.

    This function binds SQLAlchemy models to the active engine
    and creates all tables defined in the Models layer.

    Enterprise Rule:
    - No direct execution
    - No secondary entrypoints
    - Called only from controlled bootstrap flow
    """
    Base.metadata.create_all(bind=engine)
