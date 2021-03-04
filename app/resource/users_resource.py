from . import Rpta
from flask_restful import Resource
from flask import Flask, request
from app.controller.users_controller import UsersController


class UsersResourceCreate(Resource):
    def post(self):
        try:
            data = request.get_json()
            username = data["username"]
            password = data["password"]
            rpta = UsersController.create(username, password)
            return rpta.toJson()
        except Exception as e:
            answer = Rpta()
            answer.setError("Couldn't create a user",
                            "Error : {}".format(str(e)))


class UsersResourceList(Resource):
    def get(self):
        try:
            print("in list")
            data = request.get_json()
            rpta = UsersController.list()
            return rpta.toJson()
        except Exception as e:
            answer = Rpta()
            answer.setError("Couldn't get the users list",
                            "Error : {}".format(str(e)))


class UsersResourceLogin(Resource):
    def get(self):
        try:
            data = request.get_json()
            username = data["username"]
            password = data["password"]
            rpta = UsersController.login(username, password)
            return rpta.toJson()
        except Exception as e:
            answer = Rpta()
            answer.setError("Couldn't login the user",
                            "Error : {}".format(str(e)))
