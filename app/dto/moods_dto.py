from dataclasses import dataclass
from typing import Dict, List
from datetime import datetime
from app.models.mood import Mood


@dataclass
class MoodDTO():
    id_mood: int = None
    mood_name: str = None
    created_date: datetime = None
    modified_date: datetime = None
    id_user: int = None

    def to_json(self) -> Dict:
        d = {}
        for key, value in self.__dict__.items():
            if key == "created_date" or key == "modified_date":
                d[key] = value.__str__()
            else:
                d[key] = value
        return d

    @classmethod
    def from_model(cls, mood: Mood):
        d = cls(
            id_mood=mood.id_user,
            mood_name=mood.garment_name,
            created_date=mood.created_date,
            modified_date=mood.modified_date,
            id_user=mood.id_user
        )
        return d
