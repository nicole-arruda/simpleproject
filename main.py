from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional


class Game(BaseModel):
    name: str
    ID: Optional[int] = None


gameList = [Game(name="Monopoly", ID=1), Game(name="Risk", ID=2), Game(name="YAHTZEE", ID=3),
            Game(name="Settlers of Catan", ID=4), Game(name="LIFE", ID=5)]
next_id = 6


app = FastAPI()


@app.get("/games/")
async def root():
    return gameList


@app.get("/games/{search_id}")
async def game_by_id(search_id: int):
    found_game = "ID not found"
    found = False
    for game in gameList:
        if game.ID == search_id:
            found_game = game
            found = True
    if found:
        return found_game
    else:
        raise HTTPException(404, "ID not found")


@app.post("/games/")
async def new_game(new_game_name: Game):
    global next_id
    new_game_name.ID = next_id
    gameList.append(new_game_name)
    next_id += 1
    return gameList
