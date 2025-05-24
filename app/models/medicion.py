from sqlalchemy import Column, Integer, Float, DateTime, ForeignKey, TIMESTAMP
from sqlalchemy.orm import relationship
from app.config.database import Base

class Medicion(Base):
    __tablename__ = "mediciones"

    id = Column(Integer, primary_key=True, autoincrement=True)
    pozo_id = Column(Integer, ForeignKey("pozos.id", ondelete="CASCADE"), nullable=False)
    fecha = Column(DateTime, nullable=False)
    gasto = Column(Float)
    acumulado = Column(Float)
    created_at = Column(TIMESTAMP, server_default="CURRENT_TIMESTAMP")

    # Relación con Pozo
    pozo = relationship("Pozo", back_populates="mediciones")
