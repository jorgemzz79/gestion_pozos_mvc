from sqlalchemy import Column, Integer, Float, DateTime, ForeignKey, String
from sqlalchemy.orm import relationship
from app.config.database import Base

class Medicion(Base):
    __tablename__ = "mediciones"

    id = Column(Integer, primary_key=True, index=True)
    pozo_id = Column(Integer, ForeignKey("pozos.id"))
    fecha = Column(DateTime)
    tipo_medicion = Column("tipo", String(50))  # <- ¡Este es el que te falta!
    valor = Column(Float)
    unidad_id = Column(Integer, ForeignKey("unidades.id"))
    created_at = Column(DateTime)

    pozo = relationship("Pozo", back_populates="mediciones")
    unidad = relationship("Unidad")
