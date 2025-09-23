# app/routes/archivo_relacion_routes.py
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List, Optional

from app.config.database import get_db
from app.models.archivo_relacion import ArchivoRelacion
from app.models.archivo import Archivo
from app.schemas.archivo_relacion_schema import (
    ArchivoRelacionCreate, ArchivoRelacionUpdate, ArchivoRelacionResponse,
    ArchivoConRelacionResponse,   # 👈 importa el nuevo schema de respuesta
)

from app.auth.dependencies import get_current_user  # ✅ agregado
from app.models.usuario import Usuario              # ✅ agregado

router = APIRouter()

@router.post("/", response_model=ArchivoRelacionResponse)
def create_archivo_relacion(
    archivo_relacion: ArchivoRelacionCreate,
    db: Session = Depends(get_db),
    usuario: Usuario = Depends(get_current_user)  # ✅ agregado
):
    new_relacion = ArchivoRelacion(**archivo_relacion.dict())
    db.add(new_relacion)
    db.commit()
    db.refresh(new_relacion)
    return new_relacion

# ⬇️ Cambiado: ahora devuelve ArchivoConRelacionResponse (archivo + relacion_id)
@router.get("/", response_model=List[ArchivoConRelacionResponse])
def get_archivos_relacionados(
    pozo_id: Optional[int] = Query(None),
    db: Session = Depends(get_db),
    usuario: Usuario = Depends(get_current_user)  # ✅ agregado
):
    if pozo_id is None:
        raise HTTPException(status_code=400, detail="Debe especificar el pozo_id")

    relaciones = (
        db.query(ArchivoRelacion)
          .filter(ArchivoRelacion.pozo_id == pozo_id)
          .all()
    )

    resultado: list[ArchivoConRelacionResponse] = []
    for rel in relaciones:
        if not rel.archivo:
            continue
        resultado.append(ArchivoConRelacionResponse(
            relacion_id=rel.id,                       # 👈 id de archivos_relaciones
            id=rel.archivo.id,                        # id del archivo
            nombre_archivo=rel.archivo.nombre_archivo,
            tipo_archivo=rel.archivo.tipo_archivo,
            ruta_archivo=rel.archivo.ruta_archivo,
            categoria=rel.archivo.categoria,
            descripcion=rel.archivo.descripcion,
            fecha_subida=rel.archivo.fecha_subida,
        ))

    return resultado

@router.get("/{relacion_id}", response_model=ArchivoRelacionResponse)
def get_archivo_relacion(
    relacion_id: int,
    db: Session = Depends(get_db),
    usuario: Usuario = Depends(get_current_user)  # ✅ agregado
):
    relacion = db.query(ArchivoRelacion).filter(ArchivoRelacion.id == relacion_id).first()
    if not relacion:
        raise HTTPException(status_code=404, detail="Relación de archivo no encontrada")
    return relacion

@router.put("/{relacion_id}", response_model=ArchivoRelacionResponse)
def update_archivo_relacion(
    relacion_id: int,
    relacion_data: ArchivoRelacionUpdate,
    db: Session = Depends(get_db),
    usuario: Usuario = Depends(get_current_user)  # ✅ agregado
):
    relacion = db.query(ArchivoRelacion).filter(ArchivoRelacion.id == relacion_id).first()
    if not relacion:
        raise HTTPException(status_code=404, detail="Relación de archivo no encontrada")

    for key, value in relacion_data.dict(exclude_unset=True).items():
        setattr(relacion, key, value)

    db.commit()
    db.refresh(relacion)
    return relacion

@router.delete("/{relacion_id}")
def delete_archivo_relacion(
    relacion_id: int,
    db: Session = Depends(get_db),
    usuario: Usuario = Depends(get_current_user)  # ✅ agregado
):
    relacion = db.query(ArchivoRelacion).filter(ArchivoRelacion.id == relacion_id).first()
    if not relacion:
        raise HTTPException(status_code=404, detail="Relación de archivo no encontrada")

    db.delete(relacion)
    db.commit()
    return {"message": "Relación de archivo eliminada exitosamente"}
