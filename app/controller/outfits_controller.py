from app.resource import Rpta
from app.data_access import CommandDB, transactional
from typing import List, Dict

import random


class OutfitsController:

    def create():
        print("create")

    # Generates a new outfit

    @transactional
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

    def list():
        print("list")

    def get_one():
        print("get one")

    def edit():
        print("edit")

    def delete():
        print("delete")
