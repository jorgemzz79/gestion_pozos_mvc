from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from typing import List

from app.auth.dependencies import get_current_user
from app.config.database import get_db
from app.models.catalogo_mod_rep import CatalogoModRep
from app.models.usuario import Usuario
from app.schemas.catalogo_mod_rep_schema import CatalogoModRepResponse

router = APIRouter()


@router.get("/", response_model=List[CatalogoModRepResponse])
def get_catalogo_mod_rep(
    incluir_inactivos: bool = Query(False),
    db: Session = Depends(get_db),
    usuario: Usuario = Depends(get_current_user),
):
    query = db.query(CatalogoModRep)
    if not incluir_inactivos:
        query = query.filter(CatalogoModRep.activo == True)
    return query.order_by(CatalogoModRep.id).all()
