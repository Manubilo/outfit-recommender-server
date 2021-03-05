from dataclasses import dataclass
from typing import Dict, List
from datetime import datetime
from app.models.user import User


@dataclass
class UserDTO():
    id_user: int = None
    username: str = None
    password: str = None
    created_date: datetime = None

    def to_json(self) -> Dict:
        d = {}
        for key, value in self.__dict__.items():
            if key == "created_date":
                d[key] = value.__str__()
            else:
                d[key] = value
        return d

    @classmethod
    def from_model(cls, user: User):
        d = cls(
            id_user=user.id_user,
            username=user.username,
            password=user.password,
            created_date=user.created_date
        )
        return d
