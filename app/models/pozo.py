from sqlalchemy import Column, Integer, String, Date, DECIMAL, TIMESTAMP, ForeignKey
from sqlalchemy.orm import relationship
from app.config.database import Base

class Pozo(Base):
    __tablename__ = "pozos"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre_pozo = Column(String(100), nullable=False)
    comunidad = Column(String(100))
    fecha_perforacion = Column(Date)
    domicilio = Column(String(200))
    latitud = Column(DECIMAL(9, 6))
    longitud = Column(DECIMAL(9, 6))
    altitud = Column(Integer)
    profundidad = Column(DECIMAL(10, 2))
    gasto_actual_id = Column(Integer)
    diametro_ademe = Column(String(255))
    longitud_ademe_ciego = Column(String(255))
    longitud_ademe_ranurado = Column(String(255))
    tren_descarga = Column(String(255))
    concesion = Column(String(255))
    created_at = Column(TIMESTAMP, server_default="CURRENT_TIMESTAMP")
    updated_at = Column(TIMESTAMP, server_default="CURRENT_TIMESTAMP", onupdate="CURRENT_TIMESTAMP")
    tren_descarga = Column(String(255))
    concesion = Column(String(255))
    # Relaciones
    motores = relationship("Motor", back_populates="pozo", cascade="all, delete")
    recibos_luz = relationship("ReciboLuz", back_populates="pozo", cascade="all, delete")
    mediciones = relationship("Medicion", back_populates="pozo", cascade="all, delete")
    modificaciones_reparaciones = relationship("ModificacionReparacion", back_populates="pozo", cascade="all, delete")
    niveles = relationship("Nivel", back_populates="pozo", cascade="all, delete")
    transformadores = relationship("Transformador", back_populates="pozo", cascade="all, delete")
    almacenamiento = relationship("Almacenamiento", back_populates="pozo", cascade="all, delete")
    archivos = relationship("ArchivoRelacion", back_populates="pozo", cascade="all, delete")
