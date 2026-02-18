from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

load_dotenv(override=True)

POSTGRES_URL = os.getenv("POSTGRES_URL")

# Use Postgres if URL is provided, fallback to SQLite for local dev
if POSTGRES_URL:
    # Some providers use 'postgres://' but SQLAlchemy needs 'postgresql://'
    if POSTGRES_URL.startswith("postgres://"):
        POSTGRES_URL = POSTGRES_URL.replace("postgres://", "postgresql://", 1)
    DATABASE_URL = POSTGRES_URL
    print("✅ Connected to Postgres database.")
else:
    print("⚠️  No POSTGRES_URL found. Using SQLite for local development.")
    DATABASE_URL = "sqlite:///./users.db"

connect_args = {"check_same_thread": False} if "sqlite" in DATABASE_URL else {}
engine = create_engine(DATABASE_URL, connect_args=connect_args)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
