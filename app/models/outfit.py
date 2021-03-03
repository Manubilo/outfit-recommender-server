from . import db
from sqlalchemy import func
from app.models.user import User


class Outfit(db.Model):
    __tablename__ = "T_OUTFIT"
    id_outfit = db.Column("id_outfit", db.Integer, primary_key=True)
    outfit_name = db.Column("outfit_name", db.String(100), nullable=True)
    created_date = db.Column("created_date", db.DateTime,
                             nullable=True, default=func.current_timestamp())
    modified_date = db.Column("modified_date", db.DateTime, nullable=True)
    id_user = db.Column(
        'id_user', db.ForeignKey(User.id_user))  # FK
