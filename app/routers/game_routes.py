from typing import List

from app.utils import SQUARE_TYPE
from fastapi import APIRouter, Body, HTTPException, status
from fastapi.responses import JSONResponse
from app.dtos.accounts import AccountDTO
from app.dtos.piece import (
    PieceDTO,
    encode_piece_for_network,
    encode_pieces_for_network,
    filter_pieces_on_board,
    parse_encoded_pieces,
)
from app.schemas import games

router = APIRouter()


@router.post("/{game_id}")
async def create_game(game_id: int, players: list[AccountDTO]):
    assert not len(players) == 2
    

@router.get("/{game_id}")
async def get_moves(game_id: int): ...


@router.get("/{game_id}")
async def get_board_position(game_id: int):
    game = await games.fetch_by_id(game_id)

    if not game:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Game not found"
        )

    pieces = parse_encoded_pieces(game["encoded_pieces"])

    pieces_on_board = filter_pieces_on_board(pieces)

    network_encoded_pieces = encode_pieces_for_network(pieces_on_board)

    response = JSONResponse(
        status_code=status.HTTP_200_OK,
        content={"network_encoded_pieces": network_encoded_pieces},
    )

    return response


# @router.post("/{game_id}/moves")
# async def make_move(game_id: int, move: Move): ...


@router.get("/games")
async def get_all_games():
    all_games = await games.fetch_all()

    response = JSONResponse(
        status_code=status.HTTP_200_OK, content={"all_games": all_games}
    )

    return response


@router.get("/{game_id}")
async def get_game(game_id: int): ...


@router.put("/{game_id}")
async def update_game(game_id: int): ...


@router.delete("/{game_id}")
async def delete_game(game_id: int): ...
