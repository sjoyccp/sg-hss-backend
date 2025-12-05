from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from datetime import datetime, timedelta
from jose import jwt
from app.services.auth import authenticate_user   # ✅ IMPORT CORRETO

router = APIRouter()

SECRET = "segredo"
ALGORITHM = "HS256"

class LoginIn(BaseModel):
    email: str
    senha: str

@router.post("/login")
def login(data: LoginIn):
    user = authenticate_user(data.email, data.senha)  # ✅ CHAMADA CORRETA
    if not user:
        raise HTTPException(status_code=401, detail="Credenciais inválidas")

    token = jwt.encode(
        {"sub": user.email, "role": user.papel, "exp": datetime.utcnow() + timedelta(hours=1)},
        SECRET,
        algorithm=ALGORITHM
    )
    return {"access_token": token, "token_type": "bearer"}

