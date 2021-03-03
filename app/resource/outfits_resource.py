from . import Rpta
from flask_restful import Resource
from flask import Flask, request
from app.controller.outfits_controller import OutfitController


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
