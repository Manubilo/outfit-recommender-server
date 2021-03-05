from app.models import db
from typing import Dict, List, Tuple
from app.models.outfit_x_garment import Outfit_x_Garment


class Outfit_x_GarmentDataAccess:

    def create(id_outfit: int, id_garment: int):
        try:
            outfit_x_garment: Outfit_x_Garment
            outfit_x_garment = Outfit_x_Garment(
                id_outfit=id_outfit,
                id_garment=id_garment
            )
            db.session.add(outfit_x_garment)
            db.session.flush()
        except Exception as e:
            raise e

    def list(id_outfit: int):
        try:
            return Outfit_x_Garment.query.filter(
                Outfit_x_Garment.id_outfit == id_outfit).all()
        except Exception as e:
            raise e
