from . import db
from sqlalchemy import func
from app.models.user import User


class Mood(db.Model):
    __tablename__ = "T_MOOD"
    id_mood = db.Column("id_mood", db.Integer, primary_key=True)
    mood_name = db.Column("mood_name", db.String(100), nullable=True)
    created_date = db.Column("created_date", db.DateTime,
                             nullable=True, default=func.current_timestamp())
    modified_date = db.Column("modified_date", db.DateTime, nullable=True)
    id_user = db.Column(
        'id_user', db.ForeignKey(User.id_user))  # FK
