from . import db
from sqlalchemy import func
from app.models.garment import Garment
from app.models.mood import Mood


class Garment_x_Mood(db.Model):
    __tablename__ = "T_GARMENT_X_MOOD"
    id_garment_x_mood = db.Column(
        'id_garment_x_mood', db.Integer, primary_key=True)
    id_garment = db.Column(
        'id_garment', db.ForeignKey(Garment.id_garment))  # FK
    id_mood = db.Column(
        'id_mood', db.ForeignKey(Mood.id_mood))  # FK
