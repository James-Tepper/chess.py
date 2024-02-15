from fastapi import APIRouter, Body
from app.dtos.piece import PieceDTO, encode_piece_for_network

router = APIRouter()


@router.get("/{game_id}/moves")
async def get_moves(game_id: int): ...


@router.post("/{game_id}/moves")
async def make_move(game_id: str, piece: PieceDTO = Body(...)):
    encoded_piece = encode_piece_for_network(piece)


@router.get("/{game_id}/moves/{move_id}")
async def get_move(game_id: str, move_id: str): ...


@router.put("/{game_id}/moves/{move_id}")
async def update_move(game_id: str, move_id: str): ...


@router.delete("/{game_id}/moves/{move_id}")
async def delete_move(game_id: str, move_id: str): ...
