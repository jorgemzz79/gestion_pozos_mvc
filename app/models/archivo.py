from sqlalchemy import Column, Integer, String, TIMESTAMP
from app.config.database import Base

class Archivo(Base):
    __tablename__ = "archivos"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre_archivo = Column(String(255), nullable=False)
    tipo_archivo = Column(String(50))
    ruta_archivo = Column(String(500))
    categoria = Column(String(50))
    descripcion = Column(String(500))
    fecha_subida = Column(TIMESTAMP, server_default="CURRENT_TIMESTAMP")
