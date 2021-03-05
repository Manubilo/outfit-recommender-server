from app.resource import Rpta
from app.data_access import CommandDB, transactional
from typing import List, Dict

from app.data_access.moods_data_access import MoodsDataAccess
from app.data_access.users_data_access import UsersDataAccess


class MoodsController:

    @transactional
    def create(id_user: int, mood_name: str):
        answer = Rpta()
        # Check if user exists
        print("got here")
        MoodsDataAccess.create(id_user, mood_name)
        answer.setOk("Mood was created")
        return answer

    @transactional
    def list():
        print("list")

    @transactional
    def get_one():
        print("list")

    @transactional
    def edit():
        print("list")

    @transactional
    def delete():
        print("list")
