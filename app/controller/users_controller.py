from app.resource import Rpta
from app.data_access import CommandDB, transactional
from typing import List, Dict


from app.data_access.users_data_access import UsersDataAccess


class UsersController:

    @transactional
    def create(username: str, password: str) -> Rpta:
        answer = Rpta()
        ph = PasswordHasher()
        hash = ph.hash(password)
        UsersDataAccess.create(username, hash)
        answer.setOk("User was created")
        return answer

    @transactional
    def list() -> Rpta:
        answer = Rpta()
        users = UsersDataAccess.list()
        res = {
            "users": users
        }
        answer.setOk("Got list of users")
        answer.setBody(res)

        return answer

    @transactional
    def login(username: str, password: str) -> Rpta:
        answer = Rpta()
        logged = UsersDataAccess.login(username, password)
        if logged:
            answer.setOk("Login successful")
        else:
            answer.setOk("Username or password is incorrect")
        return answer
