from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from app.config.database import Base

class ArchivoRelacion(Base):
    __tablename__ = "archivos_relaciones"

    id = Column(Integer, primary_key=True, autoincrement=True)
    archivo_id = Column(Integer, ForeignKey("archivos.id", ondelete="CASCADE"), nullable=False)
    pozo_id = Column(Integer, ForeignKey("pozos.id", ondelete="CASCADE"), nullable=True)
    recibo_luz_id = Column(Integer, ForeignKey("recibos_luz.id", ondelete="CASCADE"), nullable=True)
    medicion_id = Column(Integer, ForeignKey("mediciones.id", ondelete="CASCADE"), nullable=True)
    modificacion_reparacion_id = Column(Integer, ForeignKey("modificaciones_reparaciones.id", ondelete="CASCADE"), nullable=True)

    # Relaciones
    archivo = relationship("Archivo")
    pozo = relationship("Pozo", back_populates="archivos")
    recibo_luz = relationship("ReciboLuz")
    medicion = relationship("Medicion")
    modificacion_reparacion = relationship("ModificacionReparacion")
