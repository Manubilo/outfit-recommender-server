from . import db
from sqlalchemy import func
from app.models.user import User


class Garment(db.Model):
    __tablename__ = "T_GARMENT"
    id_garment = db.Column("id_garment", db.Integer, primary_key=True)
    garment_name = db.Column("garment_name", db.String(100), nullable=True)
    garment_type = db.Column("garment_type", db.String(100), nullable=True)
    created_date = db.Column("created_date", db.DateTime,
                             nullable=True, default=func.current_timestamp())
    modified_date = db.Column("modified_date", db.DateTime, nullable=True)
    id_user = db.Column(
        'id_user', db.ForeignKey(User.id_user))  # FK
