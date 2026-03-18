import random
import string

import httpx

from sqlalchemy.orm import Session

from app.schema import *
from app.models import *

class Handle():
    def __init__(self, data: AbilityInput, prefix_url: str, db: Session):
        self.data = data
        self.prefix_url = prefix_url
        self.db = db

    async def handle(self) -> dict:
        url:str = f"{self.prefix_url}/{self.data.pokemon_ability_id}"
        async with httpx.AsyncClient() as client:
            response = await client.get(url)
        
        result = response.json()
        effect_entries = result["effect_entries"]
        pokemon_list = self.transform_pokemon(result["pokemon"])
        return {
            "raw_id": self.data.raw_id,
            "user_id": self.data.user_id,
            "returned_entries": effect_entries,
            "pokemon_list": pokemon_list
        }
    
    def transform_pokemon(self, pokemon_list: list[dict]) -> list[str]:
        pokemon_result = []
        for pokemon in pokemon_list:
            name = pokemon["pokemon"]["name"]
            pokemon_result.append(name)
        return pokemon_result
    
    async def insert_to_db(self, processed_data: dict):
        len_data: int = len(processed_data["returned_entries"])
        for i in range(len_data):
            new_record = self.normalize_data(
                processed_data = processed_data,
                index = i
            )
        
            self.db.add(new_record)
            self.db.commit()
            self.db.refresh(new_record)

    def normalize_data(self, processed_data: dict, index: int) -> PokemonAbility:
        # Generate raw_id
        if index == 0:
            raw_id = processed_data["raw_id"]
        else:
            raw_id = ''.join(random.choices(string.ascii_letters + string.digits, k=13))
        # Parse Column
        user_id = processed_data["user_id"]
        pokemon_ability_id = self.data.pokemon_ability_id
        effect = processed_data["returned_entries"][index]["effect"]
        language = processed_data["returned_entries"][index]["language"]
        short_effect = processed_data["returned_entries"][index]["short_effect"]

        return PokemonAbility(
            raw_id = raw_id,
            user_id = user_id,
            pokemon_ability_id = pokemon_ability_id,
            effect = effect,
            language = language,
            short_effect = short_effect
        )