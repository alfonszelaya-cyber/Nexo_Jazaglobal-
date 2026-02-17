
# ============================================================
# ZYRA / NEXO
# DATABASE INITIALIZER — ENTERPRISE 3.0
# ============================================================

from app.database import engine
from app.Models.base import Base

# Importa todos los modelos aquí
from app.Models.user_model import User


def init_db():
    """
    Crea todas las tablas en la base de datos.
    """
    Base.metadata.create_all(bind=engine)


if __name__ == "__main__":
    init_db()
