from app.models import db
from typing import Dict, List, Tuple
from app.models.mood import Mood


class MoodsDataAccess:

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
            return garment.id_garment
        except Exception as e:
            raise e

    def list(id_user: int) -> List[Garment]:
        try:
            return Garment.query.filter(Garment.id_user == id_user).all()
        except Exception as e:
            raise e

    def get_one(id_user: int, mood_name: str):
        try:
            return Mood.query.filter(Mood.id_user == id_user, Mood.mood_name == mood_name).first()
        except Exception as e:
            raise e
