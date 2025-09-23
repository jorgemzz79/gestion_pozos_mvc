from fastapi import APIRouter, HTTPException
from fastapi.responses import FileResponse
import os

router = APIRouter()

@router.get("/ver-archivo/{carpeta}/{nombre_archivo}")
def ver_archivo(carpeta: str, nombre_archivo: str):
    base_path = "uploads"
    ruta = os.path.join(base_path, carpeta, nombre_archivo)

    if not os.path.isfile(ruta):
        raise HTTPException(status_code=404, detail="Archivo no encontrado")

    # Detectar tipo MIME
    ext = nombre_archivo.lower().split('.')[-1]
    tipos = {
        'pdf': 'application/pdf',
        'jpg': 'image/jpeg',
        'jpeg': 'image/jpeg',
        'png': 'image/png',
        'webp': 'image/webp'
    }
    media_type = tipos.get(ext, 'application/octet-stream')

    return FileResponse(path=ruta, media_type=media_type)
