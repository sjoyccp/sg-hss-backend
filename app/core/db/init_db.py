from app.core.db.base import Base
from app.core.db.session import engine
from app.core.db.models.user import Usuario  # força a criação da tabela

def create_tables():
    Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    create_tables()
    print("Tabelas criadas com sucesso!")

