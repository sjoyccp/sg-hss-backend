from app.core.db.session import SessionLocal
from app.core.db.models.user import Usuario
from app.services.auth import hash_password

def create_admin():
    db = SessionLocal()

    admin = Usuario(
        nome="Admin",
        email="admin@teste.com",
        senha_hash=hash_password("123456"),
        papel="admin"
    )

    db.add(admin)
    db.commit()
    db.close()

    print("Admin criado com sucesso!")

if __name__ == "__main__":
    create_admin()



