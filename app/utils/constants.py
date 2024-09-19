from enum import IntEnum, StrEnum
from typing import Any, Dict, List, Literal, Type

from app.chess_piece import Bishop, ChessPiece, King, Knight, Pawn, Queen, Rook

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


class SquareStatus(IntEnum):
    EMPTY = 0
    OCCUPIED_BY_OPPONENT_PIECE = 1
    OCCUPIED_BY_OWN_PIECE = 2


# TODO fix offset for idx
class StartingRank(IntEnum):
    WHITE_PAWN = 1
    WHITE_PIECES = 0

    BLACK_PAWN = 6
    BLACK_PIECES = 7


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

SQUARE_TYPE = Literal[
    "A1", "A2", "A3", "A4", "A5", "A6", "A7", "A8",
    "B1", "B2", "B3", "B4", "B5", "B6", "B7", "B8",
    "C1", "C2", "C3", "C4", "C5", "C6", "C7", "C8",
    "D1", "D2", "D3", "D4", "D5", "D6", "D7", "D8",
    "E1", "E2", "E3", "E4", "E5", "E6", "E7", "E8",
    "F1", "F2", "F3", "F4", "F5", "F6", "F7", "F8",
    "G1", "G2", "G3", "G4", "G5", "G6", "G7", "G8",
    "H1", "H2", "H3", "H4", "H5", "H6", "H7", "H8"
]

STARTING_POSITION: Dict[PieceName, Dict[PieceColor, List[str]]] = {
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

