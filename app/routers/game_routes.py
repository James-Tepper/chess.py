from fastapi import APIRouter

router = APIRouter()


@router.get("/{game_id}/moves")
async def get_moves(game_id: int):
    ...

@router.post("/{game_id}/moves")
async def make_move(game_id: int):
    ...
