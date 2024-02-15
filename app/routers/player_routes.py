from fastapi import APIRouter, HTTPException, status
from fastapi.responses import JSONResponse

from app.schemas import accounts

# implement redis for players

router = APIRouter()


@router.get("/games/{game_id}/players")
async def get_both_players(game_id: int):
    players = await accounts.fetch_account_by_game_id(game_id)

    if players is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Game not found"
        )

    white = players["white"]
    black = players["black"]

    if white is None or black is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Player not found"
        )

    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={"game_id": game_id, "players": {"white": white, "black": black}},
    )


@router.get("/games/{game_id}/players/{player_id}")
async def get_player(game_id: int, player_id: int): ...


@router.post("/games/{game_id}/players")
async def add_player(game_id: int):
    ...
    # might scrap and just create game instance at once
    # if invite or matchmaking (incorporate rating matching/algorithm?)


@router.delete("/games/{game_id}/players/{player_id}")
async def remove_player(game_id: int, player_id: int): ...
