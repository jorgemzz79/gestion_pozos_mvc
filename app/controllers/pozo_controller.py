from sqlalchemy.orm import Session
from app.models.pozo import Pozo
from app.models.pozo import Pozo
from sqlalchemy.orm import Session
from app.schemas.pozo_schema import PozoCreate



class PozoController:
    @staticmethod
    def get_all_pozos(db: Session):
        return db.query(Pozo).all()

    @staticmethod
    def create_pozo(db: Session, pozo_data: PozoCreate):
        nuevo_pozo = Pozo(**pozo_data.model_dump())
        db.add(nuevo_pozo)
        db.commit()
        db.refresh(nuevo_pozo)
        return nuevo_pozo
@staticmethod
def get_pozo_by_id(db: Session, pozo_id: int):
    pozo = db.query(Pozo).filter(Pozo.id == pozo_id).first()
    return pozo
