from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.config.database import Base

class Almacenamiento(Base):
    __tablename__ = "almacenamiento"

    id = Column(Integer, primary_key=True, autoincrement=True)
    pozo_id = Column(Integer, ForeignKey("pozos.id", ondelete="CASCADE"), nullable=False)
    tipo_almacenamiento = Column(String(255))
    lat = Column(String(255))
    lon = Column(String(255))
    capacidad_m3 = Column(String(255))
    diametro_linea = Column(String(255))

    # Relación con Pozo
    pozo = relationship("Pozo", back_populates="almacenamiento")
