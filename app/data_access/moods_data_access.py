from app.models import db
from typing import Dict, List, Tuple
from app.models.mood import Mood


class MoodsDataAccess:

    def create(id_user: int, mood_name: str):
        try:
            mood: Mood
            mood = Mood(
                mood_name=mood_name,
                id_user=id_user
            )
            db.session.add(mood)
            db.session.flush()
        except Exception as e:
            raise e

    def list(id_user: int) -> List[Mood]:
        try:
            return Mood.query.filter(Mood.id_user == id_user).all()
        except Exception as e:
            raise e

    def get_one(id_mood: int):
        try:
            return Mood.query.filter(Mood.id_mood == id_mood).first()
        except Exception as e:
            raise e

    def get_by_name(id_user: int, mood_name: str):
        try:
            return Mood.query.filter(Mood.id_user == id_user, Mood.mood_name == mood_name).first()
        except Exception as e:
            raise e

    def delete(id_mood: int):
        try:
            mood = MoodsDataAccess.get_one(id_mood)
            db.session.delete(mood)
            db.session.commit()
        except Exception as e:
            raise e
