from . import Rpta
from flask_restful import Resource
from flask import Flask, request
from app.controller.moods_controller import MoodsController


class MoodsResourceCreate(Resource):
    def post(self):
        try:
            data = request.get_json()
            id_user = data["id"]
            mood_name = data["moodName"]
            rpta = MoodsController.create(id_user, mood_name)
            return rpta.toJson()
        except Exception as e:
            answer = Rpta()
            answer.setError("Couldn't create a mood",
                            "Error : {}".format(str(e)))


class MoodsResourceList(Resource):
    def get(self):
        try:
            data = request.get_json()
            id_user = data["id"]
            rpta = MoodsController.list(id_user)
            return rpta.toJson()
        except Exception as e:
            answer = Rpta()
            answer.setError("Couldn't get the moods list",
                            "Error : {}".format(str(e)))


class MoodsResourceGetOne(Resource):
    def get(self):
        try:
            data = request.get_json()
            id_mood = data["id"]
            rpta = MoodsController.get_one(id_mood)
            return rpta.toJson()
        except Exception as e:
            answer = Rpta()
            answer.setError("Couldn't get the mood",
                            "Error : {}".format(str(e)))


class MoodsResourceEdit(Resource):
    def put(self):
        try:
            data = request.get_json()
            id = data["id"]
            mood = data["mood"]
            rpta = MoodsController.edit(id, mood)
            return rpta.toJson()
        except Exception as e:
            answer = Rpta()
            answer.setError("Couldn't edit the mood",
                            "Error : {}".format(str(e)))


class MoodsResourceDelete(Resource):
    def delete(self):
        try:
            data = request.get_json()
            id_mood = data["id"]
            rpta = MoodsController.delete(id_mood)
            return rpta.toJson()
        except Exception as e:
            answer = Rpta()
            answer.setError("Couldn't delete the mood",
                            "Error : {}".format(str(e)))
