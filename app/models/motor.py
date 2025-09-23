from sqlalchemy import Column, Integer, String, ForeignKey, Enum, DECIMAL
from sqlalchemy.orm import relationship
from app.config.database import Base

class Motor(Base):
    __tablename__ = "motores"

    id = Column(Integer, primary_key=True, autoincrement=True)
    pozo_id = Column(Integer, ForeignKey("pozos.id", ondelete="CASCADE"), nullable=False)
    motor = Column(String(255))
    velocidad  = Column(DECIMAL(10, 2))
    voltaje = Column(DECIMAL(10, 2))
    corriente = Column(DECIMAL(10, 2))
    marca = Column(String(255))
    modelo = Column(String(255))
    tipo = Column(String(255))
    diametro_descarga = Column(DECIMAL(10, 2))
    estado = Column(Enum("activo", "inactivo", "mantenimiento", name="estado_enum"), nullable=False, default="activo")
    fotos = Column(String(255))
    descripcion = Column(String(255))

    # Relación con Pozo
    pozo = relationship("Pozo", back_populates="motores")
