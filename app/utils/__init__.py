from utils.piece import Color, Name
from typing import Literal

POSITION_IDX = Literal[0, 1, 2, 3, 4, 5, 6, 7]


"""
Chess Naming Schema
Files = Column
Ranks = Rows
"""
FILES = ["A", "B", "C", "D", "E", "F", "G", "H"]
RANKS = ["1", "2", "3", "4", "5", "6", "7", "8"]


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


# FILE_TO_INDEX = {file: idx for file, idx in zip(FILES, range(7))}  # type: ignore

# RANK_TO_INDEX = {rank: idx for rank, idx in zip(RANKS, range(7))}  # type: ignore
