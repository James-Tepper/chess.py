from pydantic import BaseModel
from app.utils import PieceColor
from typing import List
from app.dtos.piece import PieceDTO
from app.chess_functionality import MoveDTO

class GameDTO(BaseModel):
    game_id: int
    current_player: PieceColor
    game_status: str
    winner: PieceColor | None = None
    moves: List[MoveDTO]
    board: List[PieceDTO]
