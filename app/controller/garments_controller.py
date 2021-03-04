from app.resource import Rpta
from app.data_access import CommandDB, transactional
from typing import List, Dict

from app.data_access.garments_data_access import GarmentsDataAccess


class GarmentsController:

    @transactional
    def create():
        print("create")

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
