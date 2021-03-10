from app.resource import Rpta
from app.data_access import CommandDB, transactional
from typing import List, Dict

from app.data_access.outfits_data_access import OutfitsDataAccess
from app.data_access.garments_data_access import GarmentsDataAccess
from app.data_access.outfit_x_garment_data_access import Outfit_x_GarmentDataAccess
from app.data_access.garment_x_mood_data_access import Garment_x_MoodDataAccess
from app.data_access.moods_data_access import MoodsDataAccess

from app.dto.outfits_dto import OutfitDTO
from app.dto.garments_dto import GarmentDTO


class OutfitsController:
    @transactional
    def create(id_user: int, outfit_name: str,  hat: str, top: str, bottom: str, shoe: str):
        answer = Rpta()
        id_outfit = OutfitsDataAccess.create(id_user, outfit_name)

        id_garment = GarmentsDataAccess.get_one_by_name(
            id_user, hat).id_garment
        Outfit_x_GarmentDataAccess.create(id_outfit, id_garment)

        id_garment = GarmentsDataAccess.get_one_by_name(
            id_user, top).id_garment
        Outfit_x_GarmentDataAccess.create(id_outfit, id_garment)

        id_garment = GarmentsDataAccess.get_one_by_name(
            id_user, bottom).id_garment
        Outfit_x_GarmentDataAccess.create(id_outfit, id_garment)

        id_garment = GarmentsDataAccess.get_one_by_name(
            id_user, shoe).id_garment
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

    def list(id_user: int):
        answer = Rpta()
        outfits = OutfitsDataAccess.list(id_user)
        l_outfits = []
        for outfit in outfits:
            outfit_dto: OutfitDTO
            outfit_dto = OutfitDTO.from_model(outfit)
            o = outfit_dto.to_json()

            # Search for the garments
            id_outfit = o["id_outfit"]
            l_o_x_g = Outfit_x_GarmentDataAccess.list(id_outfit)
            l_garments = []
            for o_x_g in l_o_x_g:
                id_garment = o_x_g.id_garment
                garment = GarmentsDataAccess.get_one(id_garment)
                garment_dto: GarmentDTO
                garment_dto = GarmentDTO.from_model(garment)
                g = garment_dto.to_json()
                l_g_x_m = Garment_x_MoodDataAccess.list_by_id_garment(
                    id_garment)
                l_moods = []
                for g_x_m in l_g_x_m:
                    id_mood = g_x_m.id_mood
                    mood = MoodsDataAccess.get_one(id_mood)
                    l_moods.append(mood.mood_name)
                g["moods"] = l_moods
                l_garments.append(g)
            o["garments"] = l_garments
            l_outfits.append(o)

        res = {
            "outfits": l_outfits
        }

        answer.setBody(res)
        answer.setOk("Got list of outfits")

        return answer

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
