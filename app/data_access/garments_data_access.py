from app.models import db
from typing import Dict, List, Tuple
from app.models.garment import Garment
from app.models.user import User


class GarmentsDataAccess:

    def list(id_user: int) -> List[Garment]:
        try:
            return Garment.query.filter(Garment.id_user == id_user).all()
        except Exception as e:
            raise e
