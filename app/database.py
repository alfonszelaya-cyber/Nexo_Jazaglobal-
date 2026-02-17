# ============================================================
# ZYRA / NEXO
# DATABASE CORE — ENTERPRISE 3.0
# PostgreSQL Connection Layer
# ============================================================

import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# ============================================================
# DATABASE URL (FROM RENDER ENV)
# ============================================================

DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise Exception("DATABASE_URL environment variable not set")

# ============================================================
# ENGINE CONFIGURATION
# ============================================================

engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True,
    pool_size=5,
    max_overflow=10
)

# ============================================================
# SESSION LOCAL
# ============================================================

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# ============================================================
# BASE MODEL
# ============================================================

Base = declarative_base()

# ============================================================
# DB SESSION DEPENDENCY (FASTAPI)
# ============================================================

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
