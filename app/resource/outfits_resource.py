from . import Rpta
from flask_restful import Resource
from flask import Flask, request
from app.controller.outfits_controller import OutfitsController


class OutfitsResourceCreate(Resource):
    def post(self):
        try:
            data = request.get_json()
            id_user = data["id"]
            outfit_name = data["name"]
            hat = data["hat"]
            top = data["top"]
            bottom = data["bottom"]
            shoe = data["shoe"]
            rpta = OutfitsController.create(
                id_user, outfit_name, hat, top, bottom, shoe)
            return rpta.toJson()
        except Exception as e:
            answer = Rpta()
            answer.setError("Couldn't create an outfit",
                            "Error : {}".format(str(e)))


class OutfitsResourceGenerate(Resource):
    def get(self):
        data = request.get_json()
        mood = data["mood"]
        hats = data["hats"]
        tops = data["tops"]
        bottoms = data["bottoms"]
        shoes = data["shoes"]
        rpta = OutfitsController.generate(mood, hats, tops, bottoms, shoes)
        return rpta


class OutfitsResourceList(Resource):
    def get(self):
        try:
            data = request.get_json()
            id_user = data["id"]
            print("id_user", id_user)
            rpta = OutfitsController.list(id_user)
            return rpta.toJson()
        except Exception as e:
            answer = Rpta()
            answer.setError("Couldn't get the outfits list",
                            "Error : {}".format(str(e)))


class OutfitsResourceGetOne(Resource):
    def get(self):
        try:
            data = request.get_json()
            id_outfit = data["id"]
            print("id_outfit", id_outfit)
            rpta = OutfitsController.get_one(id_outfit)
            return rpta.toJson()
        except Exception as e:
            answer = Rpta()
            answer.setError("Couldn't get the outfit",
                            "Error : {}".format(str(e)))


class OutfitsResourceEdit(Resource):
    def put(self):
        try:
            data = request.get_json()
            id = data["id"]
            hat = data["hat"]
            top = data["top"]
            bottom = data["bottom"]
            shoe = data["shoe"]
            rpta = OutfitsController.edit(id, hat, top, bottom, shoe)
            return rpta.toJson()
        except Exception as e:
            answer = Rpta()
            answer.setError("Couldn't edit the outfit",
                            "Error : {}".format(str(e)))


class OutfitsResourceDelete(Resource):
    def delete(self):
        try:
            data = request.get_json()
            id = data["id"]
            rpta = OutfitsController.delete(id)
            return rpta.toJson()
        except Exception as e:
            answer = Rpta()
            answer.setError("Couldn't delete the outfit",
                            "Error : {}".format(str(e)))
