from app.models import db
from typing import Dict, List, Tuple
from app.models.outfit import Outfit


class OutfitsDataAccess:

    def create(id_user: int, outfit_name: str):
        try:
            outfit: Outfit
            outfit = Outfit(
                outfit_name=outfit_name,
                id_user=id_user
            )
            db.session.add(outfit)
            db.session.flush()
            return outfit.id_outfit
        except Exception as e:
            raise e

    def list(id_user: int) -> List[Outfit]:
        try:
            return Outfit.query.filter(Outfit.id_user == id_user).all()
        except Exception as e:
            raise e

    def get_one(id_outfit: int):
        try:
            return Outfit.query.filter(Outfit.id_outfit == id_outfit).first()
        except Exception as e:
            raise e
