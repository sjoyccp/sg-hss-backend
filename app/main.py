from fastapi import FastAPI
from app.api.v1 import auth
from app.db import session, base

app = FastAPI(title="SGHSS API - FastAPI")

# cria as tabelas no banco SQLite
base.Base.metadata.create_all(bind=session.engine)

app.include_router(auth.router, prefix="/api/auth", tags=["auth"])

