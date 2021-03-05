from app.resource import Rpta
from app.data_access import CommandDB, transactional
from typing import List, Dict

from app.data_access.moods_data_access import MoodsDataAccess
from app.data_access.users_data_access import UsersDataAccess

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
    def get_one():
        print("list")

    @transactional
    def edit():
        print("list")

    @transactional
    def delete():
        print("list")
