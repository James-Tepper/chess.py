from enum import IntEnum, StrEnum
from itertools import product
from typing import Any, Dict, List, Literal, Type

from utils.piece import Bishop, ChessPiece, King, Knight, Pawn, Queen, Rook

PieceTypes: Dict[str, Type[ChessPiece]] = {
    "King": King,
    "Queen": Queen,
    "Rook": Rook,
    "Bishop": Bishop,
    "Knight": Knight,
    "Pawn": Pawn,
}


# Piece Attributes
class PieceColor(StrEnum):
    BLACK = "Black"
    WHITE = "White"


class PieceName(StrEnum):
    KING = "King"
    QUEEN = "Queen"
    ROOK = "Rook"
    BISHOP = "Bishop"
    KNIGHT = "Knight"
    PAWN = "Pawn"


class PieceValue(IntEnum):
    KING = 100
    QUEEN = 9
    ROOK = 5
    BISHOP = 3
    KNIGHT = 3
    PAWN = 1


"""
NOTE
Chess Naming Schema
Files = Column
Ranks = Rows
"""

FILES = ["A", "B", "C", "D", "E", "F", "G", "H"]
RANKS = ["1", "2", "3", "4", "5", "6", "7", "8"]

POSITION_IDX = Literal[0, 1, 2, 3, 4, 5, 6, 7]

FILE_TYPE = Literal["A", "B", "C", "D", "E", "F", "G", "H"]
RANK_TYPE = Literal["1", "2", "3", "4", "5", "6", "7", "8"]

SQUARE_TYPE = Literal[tuple("".join(item) for item in product(FILE_TYPE, RANK_TYPE))]  # type: ignore

STARTING_POSITION: Dict[PieceName, Dict[PieceColor, List[SQUARE_TYPE]]] = {
    PieceName.KING: {PieceColor.WHITE: ["E1"], PieceColor.BLACK: ["E8"]},
    PieceName.QUEEN: {PieceColor.WHITE: ["D1"], PieceColor.BLACK: ["D8"]},
    PieceName.ROOK: {PieceColor.WHITE: ["A1", "H1"], PieceColor.BLACK: ["A8", "H8"]},
    PieceName.BISHOP: {PieceColor.WHITE: ["C1", "F1"], PieceColor.BLACK: ["C8", "F8"]},
    PieceName.KNIGHT: {PieceColor.WHITE: ["B1", "G1"], PieceColor.BLACK: ["B8", "G8"]},
    PieceName.PAWN: {
        PieceColor.WHITE: ["A2", "B2", "C2", "D2", "E2", "F2", "G2", "H2"],
        PieceColor.BLACK: ["A7", "B7", "C7", "D7", "E7", "F7", "G7", "H7"],
    },
}

LABELED_BOARD: List[List[str]] = [
    [file + rank for file in FILES] for rank in RANKS[::-1]
]


def filter_keys(obj: Dict[str, Any], exclude: List[str]) -> Dict[Any, Any]:
    return {k: v for k, v in obj.items() if k not in exclude}
