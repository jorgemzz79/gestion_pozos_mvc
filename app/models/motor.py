from sqlalchemy import Column, Integer, String, ForeignKey, Enum
from sqlalchemy.orm import relationship
from app.config.database import Base

class Motor(Base):
    __tablename__ = "motores"

    id = Column(Integer, primary_key=True, autoincrement=True)
    pozo_id = Column(Integer, ForeignKey("pozos.id", ondelete="CASCADE"), nullable=False)
    motor = Column(String(255))
    velocidad = Column(String(255))
    voltaje = Column(String(255))
    corriente = Column(String(255))
    marca = Column(String(255))
    modelo = Column(String(255))
    tipo = Column(String(255))
    diametro_descarga = Column(String(255))
    estado = Column(Enum("activo", "inactivo", "mantenimiento", name="estado_enum"), nullable=False, default="activo")
    fotos = Column(String(255))
    descripcion = Column(String(255))

    # Relación con Pozo
    pozo = relationship("Pozo", back_populates="motores")
