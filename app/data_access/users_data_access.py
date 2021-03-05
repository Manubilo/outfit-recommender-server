from app.models import db
from typing import Dict, List, Tuple
from app.models.user import User
from argon2 import PasswordHasher


class UsersDataAccess:

    def create(username, password):
        try:
            u = User.query.filter_by(username=username).first()
            if u == None:
                user: User
                user = User(
                    username=username,
                    password=password
                )
                db.session.add(user)
                db.session.flush()
        except Exception as e:
            raise e

    def list() -> List[User]:
        try:
            return User.query.all()
        except Exception as e:
            raise e

    def login(username: str, password: str):
        try:
            u = User.query.filter_by(
                username=username).first()
            ph = PasswordHasher()
            try:
                ph.verify(u.password, password)
                return True
            except Exception as e:
                return False

        except Exception as e:
            raise e

    def get_one(id_user: int) -> bool:
        try:
            return User.query.filter(User.id_user == id_user).first()
        except Exception as e:
            raise e
