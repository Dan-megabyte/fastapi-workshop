from math import sqrt

from fastapi_workshop.card_data_helper import Card, cards
import pydantic
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def hello_world() -> str:
    return "Hello World"

def distance(loc_1: tuple[int, int], loc_2: tuple[int, int]) -> float:
    return sqrt((loc_1[0]-loc_2[0])**2 + (loc_1[0]-loc_2[0])**2)

SECRET_LOCATION = (1, 5)

times_found: int = 0

class TreasureResult(pydantic.BaseModel):
    found: bool | None = None
    distance_away: float | None = None

@app.get("/search_for_treasure", response_model_exclude_none=True)
def search_for_treasure(x: int, y: int) -> TreasureResult:
    given_location = (x, y)
    if (x, y) == SECRET_LOCATION:
        global times_found
        times_found += 1
        return TreasureResult(found=True)
    else:
        return TreasureResult(distance_away=distance(given_location, SECRET_LOCATION))

@app.get("/all_cards")
def get_all_cards() -> list[Card]:
    return cards
