from __future__ import annotations

from abc import ABC, abstractmethod
from typing import List

from utils import SQUARE_TYPE, PieceColor, PieceName, PieceValue
from utils.board import ChessBoard
from utils.move import Move


class ChessPiece(ABC):
    PIECE_NAME: PieceName
    PIECE_VALUE: PieceValue

    def __init__(self, color: PieceColor) -> None:
        self.color = color
        self.collision: bool = not self.PIECE_NAME == PieceName.KNIGHT
        self.has_moved: bool = (
            False  # Evaluating castling/en passant (Pawns, Rooks, King)
        )
        self.possible_moves: List[tuple]  # RankFile || [idx][idx]
        self.abrev: str

        piece_abrev = (
            self.PIECE_NAME[:1] if not self.PIECE_NAME == PieceName.KNIGHT else "N"
        )
        self.abrev = str(color[0:1] + piece_abrev).upper()

    @abstractmethod
    def piece_behavior(self):
        pass


    def get_valid_moves(self, board: ChessBoard, current_square: SQUARE_TYPE):
        piece_moves = self.piece_behavior()
        move = Move()
        # is_path_clear

        # king_not_in_check
        # if resolvable return check else mate GAMEOVER TODO implement
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
    PIECE_NAME = PieceName.KING
    PIECE_VALUE = PieceValue.KING

    def __init__(self, color: PieceColor) -> None:
        super().__init__(color)

    def piece_behavior(self):
        pass


class Queen(ChessPiece):
    PIECE_NAME = PieceName.QUEEN
    PIECE_VALUE = PieceValue.QUEEN

    def __init__(self, color: PieceColor) -> None:
        super().__init__(color)

    def piece_behavior(self):
        pass


class Rook(ChessPiece):
    PIECE_NAME = PieceName.ROOK
    PIECE_VALUE = PieceValue.ROOK

    def __init__(self, color: PieceColor) -> None:
        super().__init__(color)

    def piece_behavior(self):
        pass


class Bishop(ChessPiece):
    PIECE_NAME = PieceName.BISHOP
    PIECE_VALUE = PieceValue.BISHOP

    def __init__(self, color: PieceColor) -> None:
        super().__init__(color)

    def piece_behavior(self):
        pass


class Knight(ChessPiece):
    PIECE_NAME = PieceName.KNIGHT
    PIECE_VALUE = PieceValue.KNIGHT

    def __init__(self, color: PieceColor) -> None:
        super().__init__(color)

    def piece_behavior(self):
        pass


class Pawn(ChessPiece):
    PIECE_NAME = PieceName.PAWN
    PIECE_VALUE = PieceValue.PAWN

    def __init__(self, color: PieceColor) -> None:
        super().__init__(color)

    def piece_behavior(self):
        pass
