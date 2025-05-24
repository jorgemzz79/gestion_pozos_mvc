from sqlalchemy import Column, Integer, String
from app.config.database import Base

class CatalogoModRep(Base):
    __tablename__ = "catalogo_mod_rep"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(255), nullable=False)
    tipo = Column(String(255))
    descripcion = Column(String(255))
