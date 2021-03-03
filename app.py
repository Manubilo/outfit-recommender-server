from flask import Flask, request
from flask_restful import Api, Resource
import random

app = Flask(__name__)
api = Api(app)


# Controller
class OutfitController:
    def generate(mood: str, hats: list, tops: list, bottoms: list, shoes: list):
        # here i have to generate an outfit based on the garments in each of the categories
        new_hats = []
        new_tops = []
        new_bottoms = []
        new_shoes = []

        for hat in hats:
            moods = hat.get("moods")
            if mood in moods:
                new_hats.append(hat)
        hat = random.choice(new_hats)

        for top in tops:
            moods = top.get("moods")
            if mood in moods:
                new_tops.append(top)
        top = random.choice(new_tops)

        for bottom in bottoms:
            moods = bottom.get("moods")
            if mood in moods:
                new_bottoms.append(bottom)
        bottom = random.choice(new_bottoms)

        for shoe in shoes:
            moods = shoe.get("moods")
            if mood in moods:
                new_shoes.append(shoe)
        shoe = random.choice(new_shoes)

        rpta = {
            "hat": hat.get("name"),
            "top": top.get("name"),
            "bottom": bottom.get("name"),
            "shoe": shoe.get("name")
        }
        return rpta

# Resource


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


# Call to resource
api.add_resource(OutfitResourceGenerate, "/outfit/generate")


if __name__ == '__main__':
    app.run(debug=True)
