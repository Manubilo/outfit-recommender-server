from app.resource import Rpta
from app.data_access import CommandDB, transactional
from typing import List, Dict

from app.data_access.outfits_data_access import OutfitsDataAccess
from app.data_access.garments_data_access import GarmentsDataAccess
from app.data_access.outfit_x_garment_data_access import Outfit_x_GarmentDataAccess

from app.dto.outfits_dto import OutfitDTO


class OutfitsController:
    @transactional
    def create(id_user: int, outfit_name: str,  hat: str, top: str, bottom: str, shoe: str):
        answer = Rpta()
        id_outfit = OutfitsDataAccess.create(id_user, outfit_name)
        print("id_outfit", id_outfit)

        id_garment = GarmentsDataAccess.get_one_by_name(
            id_user, hat).id_garment
        print("id_garment", id_garment)
        Outfit_x_GarmentDataAccess.create(id_outfit, id_garment)

        id_garment = GarmentsDataAccess.get_one_by_name(
            id_user, top).id_garment
        print("id_garment", id_garment)
        Outfit_x_GarmentDataAccess.create(id_outfit, id_garment)

        id_garment = GarmentsDataAccess.get_one_by_name(
            id_user, bottom).id_garment
        print("id_garment", id_garment)
        Outfit_x_GarmentDataAccess.create(id_outfit, id_garment)

        id_garment = GarmentsDataAccess.get_one_by_name(
            id_user, shoe).id_garment
        print("id_garment", id_garment)
        Outfit_x_GarmentDataAccess.create(id_outfit, id_garment)

        answer.setOk("Outfit was created")

        return answer

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

    def get_one(id_outfit: int):
        answer = Rpta()
        outfit = OutfitsDataAccess.get_one(id_outfit)
        outfit_dto: OutfitDTO
        outfit_dto = OutfitDTO.from_model(outfit)
        print("outfit_dto", outfit_dto)
        o = outfit_dto.to_json()

        res = {
            "outfit": o
        }

        answer.setBody(res)
        answer.setOk("Got an outfit")
        return answer

    def edit():
        print("edit")

    def delete():
        print("delete")
