from app.resource import Rpta
from app.data_access import CommandDB, transactional
from typing import List, Dict

from app.models.garment import Garment
from app.models.mood import Mood
from app.data_access.garments_data_access import GarmentsDataAccess
from app.data_access.moods_data_access import MoodsDataAccess
from app.data_access.garment_x_mood_data_access import Garment_x_MoodDataAccess


class GarmentsController:

    @transactional
    def create(id_user: int, garment_name: str, garment_type: str, moods: List[Mood]):
        answer = Rpta()
        # Check if user exists
        u = UsersDataAccess.get_one(id_user)
        if u:
            id_garment = GarmentsDataAccess.create(
                id_user, garment_name, garment_type)
            # Create in garment_x_mood all the moods of this garment
            for mood in moods:
                id_mood = MoodsDataAcess.get_one(mood).id_mood
                Garment_x_MoodDataAccess.create(id_garment, id_mood)
            answer.setOk("Garment was created")
            return answer

    @transactional
    def list(id_user: int) -> Rpta:
        answer = Rpta()
        print("entre a list")
        garments = GarmentsDataAccess.list(id_user)
        res = {
            "garments": garments
        }
        answer.setOk("Got list of garments")
        answer.setBody(res)

        return answer

    @transactional
    def get_one():
        print("list")

    @transactional
    def edit():
        print("list")

    @transactional
    def delete():
        print("list")
