from . import Rpta
from flask_restful import Resource
from flask import Flask, request
from app.controller.garments_controller import GarmentsController


class GarmentsResourceCreate(Resource):
    def post(self):
        try:
            data = request.get_json()
            garment = data["garment"]
            moods = data["moods"]
            rpta = GarmentsController.create(garment, moods)
            return rpta.toJson()
        except Exception as e:
            answer = Rpta()
            answer.setError("Couldn't create a garment",
                            "Error : {}".format(str(e)))


class GarmentsResourceList(Resource):
    def get(self):
        try:
            data = request.get_json()
            id_user = data["id"]
            rpta = GarmentsController.list(id_user)
            return rpta.toJson()
        except Exception as e:
            answer = Rpta()
            answer.setError("Couldn't get the garments list",
                            "Error : {}".format(str(e)))


class GarmentsResourceGetOne(Resource):
    def get(self):
        try:
            data = request.get_json()
            id_garment = data["id"]
            rpta = GarmentsController.get_one(id_garment)
            return rpta.toJson()
        except Exception as e:
            answer = Rpta()
            answer.setError("Couldn't get the garment",
                            "Error : {}".format(str(e)))


class GarmentsResourceEdit(Resource):
    def put(self):
        try:
            data = request.get_json()
            id = data["id"]
            garment = data["garment"]
            moods = data["moods"]
            rpta = GarmentsController.edit(id, garment, moods)
            return rpta.toJson()
        except Exception as e:
            answer = Rpta()
            answer.setError("Couldn't edit the garment",
                            "Error : {}".format(str(e)))


class GarmentsResourceDelete(Resource):
    def delete(self):
        try:
            data = request.get_json()
            id_garment = data["id"]
            rpta = GarmentsController.delete(id_garment)
            return rpta.toJson()
        except Exception as e:
            answer = Rpta()
            answer.setError("Couldn't delete the garment",
                            "Error : {}".format(str(e)))
