from . import Rpta
from flask_restful import Resource
from flask import Flask, request
from app.controller.outfits_controller import OutfitController


class OutfitResourceCreate(Resource):
    def post(self):
        try:
            data = request.get_json()
            hat = data["hat"]
            top = data["top"]
            bottom = data["bottom"]
            shoe = data["shoe"]
            rpta = OutfitController.create(hat, top, bottom, shoe)
            return rpta.toJson()
        except Exception as e:
            answer = Rpta()
            answer.setError("Couldn't create an outfit",
                            "Error : {}".format(str(e)))


class OutfitResourceGenerate(Resource):
    def get(self):
        data = request.get_json()
        mood = data["mood"]
        hats = data["hats"]
        tops = data["tops"]
        bottoms = data["bottoms"]
        shoes = data["shoes"]
        rpta = OutfitController.generate(mood, hats, tops, bottoms, shoes)
        return rpta


class OutfitResourceList(Resource):
    def get(self):
        try:
            data = request.get_json()
            id_user = data["id"]
            rpta = OutfitController.list(id_user)
            return rpta.toJson()
        except Exception as e:
            answer = Rpta()
            answer.setError("Couldn't get outfits list",
                            "Error : {}".format(str(e)))


class OutfitResourceGetOne(Resource):
    def get(self):
        try:
            data = request.get_json()
            id_outfit = data["id"]
            rpta = OutfitController.get_one(id_outfit)
            return rpta.toJson()
        except Exception as e:
            answer = Rpta()
            answer.setError("Couldn't get the outfit",
                            "Error : {}".format(str(e)))


class OutfitResourceEdit(Resource):
    def put(self):
        try:
            data = request.get_json()
            id = data["id"]
            hat = data["hat"]
            top = data["top"]
            bottom = data["bottom"]
            shoe = data["shoe"]
            rpta = OutfitController.get_one(id, hat, top, bottom, shoe)
            return rpta.toJson()
        except Exception as e:
            answer = Rpta()
            answer.setError("Couldn't edit the outfit",
                            "Error : {}".format(str(e)))


class OutfitResourceDelete(Resource):
    def delete(self):
        try:
            data = request.get_json()
            id = data["id"]
            rpta = OutfitController.delete(id)
            return rpta.toJson()
        except Exception as e:
            answer = Rpta()
            answer.setError("Couldn't delete the outfit",
                            "Error : {}".format(str(e)))
