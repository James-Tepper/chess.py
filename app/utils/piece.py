from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Callable

from utils import SQUARE_TYPE, Color, Name, Value
from utils.board import ChessBoard


def move_validation(get_valid_moves: Callable):
    def wrapper(piece: ChessPiece, board: ChessBoard, current_square: SQUARE_TYPE):
        curr_position = board.get_index_of_square(current_square)
        curr_rank = curr_position["rank"]
        curr_file = curr_position["file"]

        # Check if the path to the position is clear
        piece_position = board.position[curr_rank][curr_file]

        # Get valid move from parent method
        unfiltered_valid_moves = get_valid_moves(piece, board, current_square)

        # TODO Filter out moves where the piece is pinned to the King

        valid_moves = [
            move
            for move in unfiltered_valid_moves
            if piece.is_path_clear(board, piece_position, move)
            and piece.not_pinned_to_king(board, piece_position)
        ]

        return valid_moves

    return wrapper


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

    @abstractmethod  # type: ignore
    @move_validation
    def get_valid_moves(self, board: ChessBoard, current_square: SQUARE_TYPE):
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
        self.value = None  # King doesn't have a value

    def get_valid_moves(self, board: ChessBoard, current_square: SQUARE_TYPE):
        pass


class Queen(ChessPiece):
    PIECE_NAME = Name.QUEEN
    PIECE_VALUE = Value.QUEEN

    def __init__(self, color: Color) -> None:
        super().__init__(color)

    def get_valid_moves(self, board: ChessBoard, current_square: SQUARE_TYPE):
        pass


class Rook(ChessPiece):
    PIECE_NAME = Name.ROOK
    PIECE_VALUE = Value.ROOK

    def __init__(self, color: Color) -> None:
        super().__init__(color)
        self.value = 5

    def get_valid_moves(self, board: ChessBoard, current_square: SQUARE_TYPE):
        pass


class Bishop(ChessPiece):
    PIECE_NAME = Name.BISHOP
    PIECE_VALUE = Value.BISHOP

    def __init__(self, color: Color) -> None:
        super().__init__(color)
        self.value = 3

    def get_valid_moves(self, board: ChessBoard, current_square: SQUARE_TYPE):
        pass


class Knight(ChessPiece):
    PIECE_NAME = Name.KNIGHT
    PIECE_VALUE = Value.KNIGHT

    def __init__(self, color: Color) -> None:
        super().__init__(color)
        self.value = 3

    def get_valid_moves(self, board: ChessBoard, current_square: SQUARE_TYPE):
        pass


class Pawn(ChessPiece):
    PIECE_NAME = Name.PAWN
    PIECE_VALUE = Value.PAWN

    def __init__(self, color: Color) -> None:
        super().__init__(color)
        self.value = 1

    def get_valid_moves(self, board: ChessBoard, current_square: SQUARE_TYPE):
        pass
