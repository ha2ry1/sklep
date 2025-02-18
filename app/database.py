from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///./shop.db" #Dla przykładu baza w SQLite

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
#W przypadku bazy innej niż SQLite skasować "connect_args={"check_same_thread": False}"
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()