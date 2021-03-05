from dataclasses import dataclass
from typing import Dict, List
from datetime import datetime
from app.models.garment import Garment


@dataclass
class GarmentDTO():
    id_garment: int = None
    garment_name: str = None
    garment_type: str = None
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
    def from_model(cls, garment: Garment):
        d = cls(
            id_garment=garment.id_user,
            garment_name=garment.garment_name,
            garment_type=garment.garment_type,
            created_date=garment.created_date,
            modified_date=garment.modified_date,
            id_user=garment.id_user
        )
        return d
