from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def get_players():
    ...

@router.get("/{player_id}")
async def get_player(player_id):
    ...

@router.post("/")
async def create_player():
    ...

@router.put("/{player_id}")
async def update_player(player_id: int):
    ...


@router.delete("/{player_id}")
async def delete_player(player_id: int):
    ...
