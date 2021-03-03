from . import db
from sqlalchemy import func
from app.models.garment import Garment
from app.models.outfit import Outfit


class Outfit_x_Garment(db.Model):
    __tablename__ = "T_OUTFIT_X_GARMENT"
    id_outfit_x_garment = db.Column(
        'id_outfit_x_garment', db.Integer, primary_key=True)
    id_outfit = db.Column(
        'id_outfit', db.ForeignKey(Garment.id_garment))  # FK
    id_mood = db.Column(
        'id_mood', db.ForeignKey(Mood.id_mood))  # FK
