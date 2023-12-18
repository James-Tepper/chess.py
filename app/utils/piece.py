from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Callable

from utils import Color, Name, Value, SQUARE_TYPE
from utils.board import ChessBoard
from utils.move import Move


class ChessPiece(ABC):
    PIECE_NAME: Name
    PIECE_VALUE: Value

    def __init__(self, color: Color) -> None:
        self.color = color
        self.collision: bool = not self.PIECE_NAME == Name.KNIGHT
        self.has_moved: bool = (
            False  # Evaluating castling/en passant (Pawns, Rooks, King)
        )
        self.possible_moves: list[tuple]  # RankFile || [idx][idx]
        self.abrev: str

        piece_abrev = (
            self.PIECE_NAME[0:1] if not self.PIECE_NAME == Name.KNIGHT else "N"
        )
        self.abrev = str(color[0:1] + piece_abrev).upper()

    @abstractmethod
    def piece_behavior(self):
        ...


    def get_valid_moves(self, board: ChessBoard, current_square: SQUARE_TYPE):
        piece_moves = self.piece_behavior()
        move = Move()
        # is_path_clear
        
        # not_pinned_to_king

        """
        NOTE: Must be called with move_validation
        TODO Check if king is directly hit by move check(color) || hit by piece moving
        """
        pass

    def is_path_clear(
        self, board: ChessBoard, current_square: SQUARE_TYPE, target_square: SQUARE_TYPE
    ):
        # TODO implement algorithm for each piece to skip over unobtainable squares
        # TODO implement || AND check for Knight
        if not self.collision:
            return True

    def not_pinned_to_king(self, board: ChessBoard, current_square: SQUARE_TYPE):
        # Find king location
        pass


class King(ChessPiece):
    PIECE_NAME = Name.KING
    PIECE_VALUE = Value.KING

    def __init__(self, color: Color) -> None:
        super().__init__(color)

    def piece_behavior(self):
        pass


class Queen(ChessPiece):
    PIECE_NAME = Name.QUEEN
    PIECE_VALUE = Value.QUEEN

    def __init__(self, color: Color) -> None:
        super().__init__(color)

    def piece_behavior(self):
        pass


class Rook(ChessPiece):
    PIECE_NAME = Name.ROOK
    PIECE_VALUE = Value.ROOK

    def __init__(self, color: Color) -> None:
        super().__init__(color)

    def piece_behavior(self):
        pass


class Bishop(ChessPiece):
    PIECE_NAME = Name.BISHOP
    PIECE_VALUE = Value.BISHOP

    def __init__(self, color: Color) -> None:
        super().__init__(color)

    def piece_behavior(self):
        pass


class Knight(ChessPiece):
    PIECE_NAME = Name.KNIGHT
    PIECE_VALUE = Value.KNIGHT

    def __init__(self, color: Color) -> None:
        super().__init__(color)

    def piece_behavior(self):
        pass


class Pawn(ChessPiece):
    PIECE_NAME = Name.PAWN
    PIECE_VALUE = Value.PAWN

    def __init__(self, color: Color) -> None:
        super().__init__(color)

    def piece_behavior(self):
        pass
