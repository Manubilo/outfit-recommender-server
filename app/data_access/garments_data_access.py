from app.models import db
from typing import Dict, List, Tuple
from app.models.garment import Garment
from app.models.user import User


class GarmentsDataAccess:

    def create(id_user: int, garment_name: str, garment_type: str):
        try:
            garment: Garment
            garment = Garment(
                garment_name=garment_name,
                garment_type=garment_type,
                id_user=id_user
            )
            db.session.add(garment)
            db.session.flush()
        except Exception as e:
            raise e

    def list(id_user: int) -> List[Garment]:
        try:
            return Garment.query.filter(Garment.id_user == id_user).all()
        except Exception as e:
            raise e
