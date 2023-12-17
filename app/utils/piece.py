from __future__ import annotations

from abc import ABC, abstractmethod
from enum import StrEnum

from utils import SQUARE_TYPE
from utils.board import ChessBoard
from typing import Callable

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

def move_validation(get_valid_moves_func: Callable):
    def wrapper(self, board: ChessBoard, current_square: SQUARE_TYPE):
        curr_position = board.get_index_of_square(current_square)
        curr_rank = curr_position["rank"]
        curr_file = curr_position["file"]

        # Check if the path to the position is clear
        start_position = board.position[curr_rank][curr_file]
        """
        self.piece match and get respective movements
        """
        ...

class ChessPiece(ABC):
    PIECE_NAME: Name

    def __init__(self, color: Color) -> None:
        self.color = color
        self.value: int | None  # None for King | if temp_val is None: game over
        self.collision: bool = not self.PIECE_NAME == Name.KNIGHT
        self.has_moved: bool = False  # Evaluating castling/en passant
        self.possible_moves: list[tuple]  # RankFile || [idx][idx]
        self.abrev: str

        piece_abrev = (
            self.PIECE_NAME[0:1] if not self.PIECE_NAME == Name.KNIGHT else "N"
        )
        self.abrev = str(color[0:1] + piece_abrev).upper()


    @abstractmethod
    def get_valid_moves(self, board: ChessBoard, current_square: SQUARE_TYPE):
        """
        NOTE: Must be called with move_validation
        TODO Check if king is directly hit by move check(color) || hit by piece moving
        """
        pass


class King(ChessPiece):
    PIECE_NAME = Name.KING

    def __init__(self, color: Color) -> None:
        super().__init__(color)
        self.value = None  # King doesn't have a value

    @move_validation
    def get_valid_moves(self, board: ChessBoard, current_square: SQUARE_TYPE):
        pass




class Queen(ChessPiece):
    PIECE_NAME = Name.QUEEN

    def __init__(self, color: Color) -> None:
        super().__init__(color)
        self.value = 9

    @move_validation
    def get_valid_moves(self, board: ChessBoard, current_square: SQUARE_TYPE):
        pass




class Rook(ChessPiece):
    PIECE_NAME = Name.ROOK

    def __init__(self, color: Color) -> None:
        super().__init__(color)
        self.value = 5

    @move_validation
    def get_valid_moves(self, board: ChessBoard, current_square: SQUARE_TYPE):
        pass




class Bishop(ChessPiece):
    PIECE_NAME = Name.BISHOP

    def __init__(self, color: Color) -> None:
        super().__init__(color)
        self.value = 3

    @move_validation
    def get_valid_moves(self, board: ChessBoard, current_square: SQUARE_TYPE):
        pass




class Knight(ChessPiece):
    PIECE_NAME = Name.KNIGHT

    def __init__(self, color: Color) -> None:
        super().__init__(color)
        self.value = 3

    @move_validation
    def get_valid_moves(self, board: ChessBoard, current_square: SQUARE_TYPE):
        pass




class Pawn(ChessPiece):
    PIECE_NAME = Name.PAWN

    def __init__(self, color: Color) -> None:
        super().__init__(color)
        self.value = 1

    @move_validation
    def get_valid_moves(self, board: ChessBoard, current_square: SQUARE_TYPE):
        pass

