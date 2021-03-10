from app.resource import Rpta
from app.data_access import CommandDB, transactional
from typing import List, Dict

from app.data_access.moods_data_access import MoodsDataAccess
from app.data_access.users_data_access import UsersDataAccess
from app.data_access.garment_x_mood_data_access import Garment_x_MoodDataAccess

from app.dto.moods_dto import MoodDTO


class MoodsController:

    @transactional
    def create(id_user: int, mood_name: str):
        answer = Rpta()
        MoodsDataAccess.create(id_user, mood_name)
        answer.setOk("Mood was created")
        return answer

    @transactional
    def list(id_user: int):
        answer = Rpta()
        moods = MoodsDataAccess.list(id_user)
        l_moods = []
        for mood in moods:
            mood_dto: MoodDTO
            mood_dto = MoodDTO.from_model(mood)
            m = mood_dto.to_json()
            l_moods.append(m)
        res = {
            "moods": l_moods
        }
        answer.setBody(res)
        answer.setOk("Moods were listed")
        return answer

    @transactional
    def get_one(id_mood: int):
        answer = Rpta()
        mood = MoodsDataAccess.get_one(id_mood)
        mood_dto: MoodDTO
        mood_dto = MoodDTO.from_model(mood)
        m = mood_dto.to_json()
        res = {
            "mood": m
        }
        answer.setBody(res)
        answer.setOk("Got a mood")
        return answer

    @transactional
    def edit():
        print("list")

    @transactional
    def delete(id_mood: int):
        answer = Rpta()
        # Delete from garment_x_mood table first
        l_g_x_m = Garment_x_MoodDataAccess.list_by_id_mood(id_mood)
        for g_x_m in l_g_x_m:
            Garment_x_MoodDataAccess.delete(g_x_m.id_garment_x_mood)
        # Then delete from mood table
        MoodsDataAccess.delete(id_mood)
        answer.setOk("Mood deleted")
        return answer
