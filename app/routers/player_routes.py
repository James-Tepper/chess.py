from fastapi import APIRouter
from app.schemas import accounts
# implement redis for players

router = APIRouter()

@router.get("/games/{game_id}/players")
async def get_both_players(game_id: int):
    players = await accounts.

@router.get("/games/{game_id}/players/{player_id}")
async def get_player(game_id: int, player_id: int):
    ...

@router.post("/games/{game_id}/players")
async def add_player(game_id: int):
    ...
    # if invite or matchmaking (incorporate rating matching/algorithm?)

@router.delete("/games/{game_id}/players/{player_id}")
async def remove_player(game_id: int, player_id: int):
    ...
