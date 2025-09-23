from fastapi import APIRouter, UploadFile, File, Depends
import os
from uuid import uuid4

from app.auth.dependencies import get_current_user  # ✅ agregado
from app.models.usuario import Usuario              # ✅ agregado

router = APIRouter()

@router.post("/archivos/upload")
async def subir_archivo(
    file: UploadFile = File(...),
    usuario: Usuario = Depends(get_current_user)  # ✅ agregado
):
    # Crear carpeta si no existe
    upload_dir = "uploads/pozos"
    os.makedirs(upload_dir, exist_ok=True)

    # Generar nombre único para evitar conflictos
    extension = file.filename.split('.')[-1]
    nombre_archivo = f"{uuid4()}.{extension}"
    ruta_relativa = f"{upload_dir}/{nombre_archivo}"

    # Guardar archivo
    with open(ruta_relativa, "wb") as buffer:
        buffer.write(await file.read())

    return {"ruta": ruta_relativa}
