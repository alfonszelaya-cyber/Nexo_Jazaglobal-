# ============================================================
# ZYRA / NEXO
# DATABASE INITIALIZER — ENTERPRISE 3.0
# Controlled Bootstrap Utility
# ============================================================

from app.database import engine, Base

# IMPORTAR MODELOS PARA QUE SQLALCHEMY LOS REGISTRE
import app.models.user_model  # NO BORRAR


def init_db() -> None:
    """
    Inicializa todas las tablas registradas en Base.
    
    Regla Enterprise:
    - No auto ejecución
    - No entrypoint secundario
    - Se llama únicamente desde main.py si es necesario
    """
    Base.metadata.create_all(bind=engine)
