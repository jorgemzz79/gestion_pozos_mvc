
from sqlalchemy import Column, Integer, String
from app.config.database import Base
from sqlalchemy.orm import relationship
from app.config.database import Base

class Unidad(Base):
    __tablename__ = "unidades"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)
    abreviatura = Column(String(10), nullable=False)

    mediciones = relationship("Medicion", back_populates="unidad")