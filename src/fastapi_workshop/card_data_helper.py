
from os import path
from typing import Literal, LiteralString

from pydantic import BaseModel, TypeAdapter


class Card(BaseModel):
    name: str
    color: list[Literal["B", "G", "R", "U", "W"]] = []
    convertedManaCost: float
    manaCost: str | None = None
    text: str | None = None
    type: str

cards: list[Card]

card_list_adapter = TypeAdapter(list[Card])

with open(path.dirname(__file__)+"/../../datasets/cards/StandardAtomicSimplified.json") as f:
    cards = card_list_adapter.validate_json("\n".join(f.readlines()))
