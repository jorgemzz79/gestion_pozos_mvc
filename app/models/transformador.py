
from sqlalchemy import Column, Integer, String, DECIMAL, ForeignKey
from sqlalchemy.orm import relationship
from app.config.database import Base

class Transformador(Base):
    __tablename__ = "transformadores"

    id = Column(Integer, primary_key=True, autoincrement=True)
    pozo_id = Column(Integer, ForeignKey("pozos.id", ondelete="CASCADE"), nullable=False)
    ubicacion = Column(String(255))
    kva = Column(Integer)
    voltage_primario = Column(DECIMAL(10, 2))
    voltage_secundario = Column(String(20))
    marca = Column(String(50))
    serie = Column(String(50))
    bomba = Column(String(50))
    modelo = Column(String(50))
    serie_bomba = Column(String(50))

    # Relación con Pozo
    pozo = relationship("Pozo", back_populates="transformadores")
