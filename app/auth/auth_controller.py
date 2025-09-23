# app/auth/auth_controller.py
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from app.config.database import get_db
from app.models.usuario import Usuario
from app.auth.auth_utils import verificar_contraseña, crear_token

router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    # Swagger enviará form_data.username y form_data.password
    db_user = db.query(Usuario).filter(Usuario.username == form_data.username).first()
    if not db_user or not verificar_contraseña(form_data.password, db_user.password_hash):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Usuario o contraseña incorrectos")

    token = crear_token({"sub": db_user.username, "rol": db_user.rol})
    return {"access_token": token, "token_type": "bearer"}

# (opcional) utilidad para generar hashes
@router.post("/generar-password/")
def generar_password(password: str):
    from app.auth.auth_utils import hashear_contraseña
    return {"hashed_password": hashear_contraseña(password)}
