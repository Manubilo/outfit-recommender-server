from app.models import db
from typing import Dict, List, Tuple
from app.models.garment_x_mood import Garment_x_Mood


class Garment_x_MoodDataAccess:

    def create(id_garment: int, id_mood: int):
        try:
            garment_x_mood: Garment_x_Mood
            garment_x_mood = Garment_x_Mood(
                id_garment=id_garment,
                id_mood=id_mood
            )
            db.session.add(garment_x_mood)
            db.session.flush()
        except Exception as e:
            raise e

    def list(id_garment: int):
        try:
            return Garment_x_Mood.query.filter(
                Garment_x_Mood.id_garment == id_garment).all()
        except Exception as e:
            raise e
