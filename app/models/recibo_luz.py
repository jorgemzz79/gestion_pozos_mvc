from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey, TIMESTAMP
from sqlalchemy.orm import relationship
from app.config.database import Base

class ReciboLuz(Base):
    __tablename__ = "recibos_luz"

    id = Column(Integer, primary_key=True, autoincrement=True)
    pozo_id = Column(Integer, ForeignKey("pozos.id", ondelete="CASCADE"), nullable=False)
    bimestre = Column(String(20))
    consumo_kwh = Column(Float, nullable=False)
    costo_total = Column(Float, nullable=False)
    fecha_pago = Column(Date)
    created_at = Column(TIMESTAMP, server_default="CURRENT_TIMESTAMP")

    # Relación con Pozo
    pozo = relationship("Pozo", back_populates="recibos_luz")