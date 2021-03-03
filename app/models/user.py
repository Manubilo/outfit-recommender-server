from . import db
from sqlalchemy import func


class User(db.Model):
    __tablename__ = "T_USER"
    id_user = db.Column("id_user", db.Integer, primary_key=True)
    username = db.Column("username", db.String(100), nullable=True)
    password = db.Column("password", db.String(100), nullable=True)
    created_date = db.Column("created_date", db.DateTime,
                             nullable=True, default=func.current_timestamp())
