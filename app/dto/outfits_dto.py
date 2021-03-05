from dataclasses import dataclass
from typing import Dict, List
from datetime import datetime
from app.models.outfit import Outfit


@dataclass
class OutfitDTO():
    id_outfit: int = None
    outfit_name: str = None
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
    def from_model(cls, outfit: Outfit):
        d = cls(
            id_outfit=outfit.id_outfit,
            outfit_name=outfit.garment_name,
            created_date=outfit.created_date,
            modified_date=outfit.modified_date,
            id_user=outfit.id_user
        )
        return d
