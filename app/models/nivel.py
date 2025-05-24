from sqlalchemy import Column, Integer, String, TIMESTAMP, ForeignKey
from sqlalchemy.orm import relationship
from app.config.database import Base

class Nivel(Base):
    __tablename__ = "niveles"

    id = Column(Integer, primary_key=True, autoincrement=True)
    pozo_id = Column(Integer, ForeignKey("pozos.id", ondelete="CASCADE"), nullable=False)
    tipo_nivel = Column(String(255))
    abatimiento = Column(String(255))
    fecha_medicion = Column(TIMESTAMP, server_default="CURRENT_TIMESTAMP")

    # Relación con Pozo
    pozo = relationship("Pozo", back_populates="niveles")
