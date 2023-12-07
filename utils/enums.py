from enum import StrEnum


class Color(StrEnum):
    BLACK = "BLACK"
    WHITE = "WHITE"


class Name(StrEnum):
    KING = "KING"
    QUEEN = "QUEEN"
    ROOK = "ROOK"
    BISHOP = "BISHOP"
    KNIGHT = "KNIGHT"
    PAWN = "PAWN"
