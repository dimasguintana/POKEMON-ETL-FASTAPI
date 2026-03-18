from pydantic import BaseModel

class AbilityInput(BaseModel):
    raw_id: str
    user_id: str
    pokemon_ability_id: int

class ResponseOutput(BaseModel):
    raw_id: str
    user_id: str
    returned_entries: list[dict]
    pokemon_list: list[str]