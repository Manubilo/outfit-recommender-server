from app.resource import Rpta
from app.data_access import CommandDB, transactional
from typing import List, Dict

from app.models.garment import Garment
from app.models.mood import Mood
from app.data_access.garments_data_access import GarmentsDataAccess
from app.data_access.moods_data_access import MoodsDataAccess
from app.data_access.garment_x_mood_data_access import Garment_x_MoodDataAccess
from app.data_access.moods_data_access import MoodsDataAccess

from app.dto.garments_dto import GarmentDTO
from app.dto.moods_dto import MoodDTO


class GarmentsController:

    @transactional
    def create(id_user: int, garment_name: str, garment_type: str, moods: List[Mood]):
        answer = Rpta()
        id_garment = GarmentsDataAccess.create(
            id_user, garment_name, garment_type)
        # Create in garment_x_mood all th   e moods of this garment
        for mood in moods:
            print("mood", mood)
            id_mood = MoodsDataAccess.get_by_name(id_user, mood).id_mood
            Garment_x_MoodDataAccess.create(id_garment, id_mood)
        answer.setOk("Garment was created")
        return answer

    @transactional
    def list(id_user: int) -> Rpta:
        answer = Rpta()
        print("entre a list")
        garments = GarmentsDataAccess.list(id_user)
        l_garments = []
        for garment in garments:
            garment_dto: GarmentDTO
            garment_dto = GarmentDTO.from_model(garment)
            g = garment_dto.to_json()

            # Get garment's moods
            id_garment = g["id_garment"]
            l_g_x_m = Garment_x_MoodDataAccess.list(id_garment)
            l_moods = []
            for g_x_m in l_g_x_m:
                id_mood = g_x_m.id_mood
                mood = MoodsDataAccess.get_one(id_mood)
                l_moods.append(mood.mood_name)

            g["moods"] = l_moods
            l_garments.append(g)

        res = {
            "garments": l_garments
        }
        answer.setOk("Got list of garments")
        answer.setBody(res)

        return answer

    @transactional
    def get_one(id_garment: int):
        answer = Rpta()
        garment = GarmentsDataAccess.get_one(id_garment)
        garment_dto: GarmentDTO
        garment_dto = GarmentDTO.from_model(garment)
        g = garment_dto.to_json()
        res = {
            "garment": g
        }
        answer.setOk("Got a garment")
        answer.setBody(res)

        return answer

    @transactional
    def edit():
        print("list")

    @transactional
    def delete():
        print("list")
