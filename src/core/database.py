# src/infrastructure/database.py
from dotenv import load_dotenv
from sqlmodel import SQLModel, create_engine, Session
from typing import Generator
import os



ENVIRONMENT = os.environ.get("ENVIRONMENT", "development")

if ENVIRONMENT == "development":
    # Load the local environment variables from .env.local
    print('Load the local environment variables from .env.local')
    load_dotenv(".env.local")
elif ENVIRONMENT == "production":
    # Load the production environment variables from .env
    print('Load the production environment variables from .env')
    load_dotenv(".env")
# La URL de la base de datos debería venir de una variable de entorno
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./database.db")

engine = create_engine(DATABASE_URL, echo=True)  # echo=True para ver las SQL queries



def create_db_and_tables():
    # Esta función solo se usa para crear las tablas si no existen.
    # En producción, las migraciones (Alembic) son preferibles.
    SQLModel.metadata.create_all(engine)


def get_session() -> Generator[Session, None, None]:
    """
    Generador para obtener una sesión de base de datos.
    Asegura que la sesión se cierre correctamente.
    """
    with Session(engine) as session:
        yield session
