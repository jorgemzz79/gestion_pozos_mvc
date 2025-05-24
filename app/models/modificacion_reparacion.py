from sqlalchemy import Column, Integer, String, TIMESTAMP, ForeignKey
from app.models.catalogo_mod_rep import CatalogoModRep
from sqlalchemy.orm import relationship
from app.config.database import Base

class ModificacionReparacion(Base):
    __tablename__ = "modificaciones_reparaciones"

    id = Column(Integer, primary_key=True, autoincrement=True)
    pozo_id = Column(Integer, ForeignKey("pozos.id", ondelete="CASCADE"), nullable=False)
    tipo_modificacion = Column(Integer, ForeignKey("catalogo_mod_rep.id", ondelete="SET NULL"), nullable=True)
    descripcion_modificacion_reparacion = Column(String(500))
    fecha = Column(TIMESTAMP, server_default="CURRENT_TIMESTAMP")
    responsable = Column(String(255))

    # Relaciones
    pozo = relationship("Pozo", back_populates="modificaciones_reparaciones")
    catalogo = relationship("CatalogoModRep")
