from pydantic import BaseModel
from enum import IntEnum






class PieceType(IntEnum):
    PAWN = 1
    KNIGHT = 2
    BISHOP = 3
    ROOK = 4
    QUEEN = 5
    KING = 6

class PieceColor(IntEnum):
    WHITE = 0
    BLACK = 1

class PieceStatus(IntEnum):
    OFF_BOARD = 0
    ON_BOARD = 1


class PieceDTO(BaseModel):
    piece_type: PieceType
    color: PieceColor
    status: PieceStatus
    rank: int # TODO prob create way to convert
    file: int
    extra: int
