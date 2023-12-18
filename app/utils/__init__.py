from enum import IntEnum, StrEnum
from typing import Literal


# Piece Attributes
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


class Value(IntEnum):
    KING = 0
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

STARTING_POSITION: dict[Name, dict[Color, list[str]]] = {
    Name.KING: {Color.WHITE: ["E1"], Color.BLACK: ["E8"]},
    Name.QUEEN: {Color.WHITE: ["D1"], Color.BLACK: ["D8"]},
    Name.ROOK: {Color.WHITE: ["A1", "H1"], Color.BLACK: ["A8", "H8"]},
    Name.BISHOP: {Color.WHITE: ["C1", "F1"], Color.BLACK: ["C8", "F8"]},
    Name.KNIGHT: {Color.WHITE: ["B1", "G1"], Color.BLACK: ["B8", "G8"]},
    Name.PAWN: {
        Color.WHITE: ["A2", "B2", "C2", "D2", "E2", "F2", "G2", "H2"],
        Color.BLACK: ["A7", "B7", "C7", "D7", "E7", "F7", "G7", "H7"],
    },
}

LABELED_BOARD: list[list[str]] = [
    [file + rank for file in FILES] for rank in RANKS[::-1]
]

# Literal Types
FILE_TYPE = Literal["A", "B", "C", "D", "E", "F", "G", "H"]
RANK_TYPE = Literal["1", "2", "3", "4", "5", "6", "7", "8"]
SQUARE_TYPE = Literal[
    "A8",
    "B8",
    "C8",
    "D8",
    "E8",
    "F8",
    "G8",
    "H8",
    "A7",
    "B7",
    "C7",
    "D7",
    "E7",
    "F7",
    "G7",
    "H7",
    "A6",
    "B6",
    "C6",
    "D6",
    "E6",
    "F6",
    "G6",
    "H6",
    "A5",
    "B5",
    "C5",
    "D5",
    "E5",
    "F5",
    "G5",
    "H5",
    "A4",
    "B4",
    "C4",
    "D4",
    "E4",
    "F4",
    "G4",
    "H4",
    "A3",
    "B3",
    "C3",
    "D3",
    "E3",
    "F3",
    "G3",
    "H3",
    "A2",
    "B2",
    "C2",
    "D2",
    "E2",
    "F2",
    "G2",
    "H2",
    "A1",
    "B1",
    "C1",
    "D1",
    "E1",
    "F1",
    "G1",
    "H1",
]
