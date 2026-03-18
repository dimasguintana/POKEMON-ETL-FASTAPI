from sqlalchemy import Column, Integer, String, Text, JSON
from app.database import Base

class PokemonAbility(Base):
    __tablename__ = "pokemon_abilities"

    id = Column(Integer, primary_key = True, index = True, autoincrement = True)
    raw_id = Column(String(13))
    user_id = Column(Integer)
    pokemon_ability_id = Column(Integer)
    effect = Column(Text)
    language = Column(JSON)
    short_effect = Column(String)