from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///./database.db"

# Criar engine (conexão com o banco)
engine = create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)

# Criar sessão
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

