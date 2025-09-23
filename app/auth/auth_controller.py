from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.config.database import get_db
from app.models.usuario import Usuario  # CORREGIDO
from app.schemas.usuario_schema import UsuarioLogin  # CORREGIDO
from app.auth.auth_utils import verificar_contraseña, crear_token
from app.auth import auth_controller  # ✅ ESTA LÍNEA FALTA
from app.auth.auth_utils import hashear_contraseña

router = APIRouter()

@router.post("/login")
def login(user: UsuarioLogin, db: Session = Depends(get_db)):
    db_user = db.query(Usuario).filter(Usuario.username == user.username).first()
    if not db_user or not verificar_contraseña(user.password, db_user.password_hash):
        raise HTTPException(status_code=401, detail="Credenciales incorrectas")
    
    token = crear_token({"sub": db_user.username, "rol": db_user.rol})
    return {"access_token": token, "token_type": "bearer"}


@router.post("/generar-password/")
def generar_password(password: str):
    hashed = hashear_contraseña(password)
    return {"hashed_password": hashed}