from __future__ import annotations

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


class ChessPiece:
    PIECE_NAME: Name

    def __init__(self, color: Color) -> None:
        self.color = color
        self.abrev: str
        
        piece_abrev = (
            self.PIECE_NAME[0:1] if not self.PIECE_NAME == Name.KNIGHT else "N"
        )
        self.abrev = str(color[0:1] + piece_abrev).upper()

    # def check_if_valid_move(self, board_state, position):
    #     # Check if king is directly hit by move check(color)
    #     ...

    def is_within_board(self, position):
        row, col = position
        return 0 <= row < 7 and 0 <= col < 7


class King(ChessPiece):
    PIECE_NAME = Name.KING

    def __init__(self, color: Color) -> None:
        super().__init__(color)


class Queen(ChessPiece):
    PIECE_NAME = Name.QUEEN

    def __init__(self, color: Color) -> None:
        super().__init__(color)


class Rook(ChessPiece):
    PIECE_NAME = Name.ROOK

    def __init__(self, color: Color) -> None:
        super().__init__(color)


class Bishop(ChessPiece):
    PIECE_NAME = Name.BISHOP

    def __init__(self, color: Color) -> None:
        super().__init__(color)


class Knight(ChessPiece):
    PIECE_NAME = Name.KNIGHT

    def __init__(self, color: Color) -> None:
        super().__init__(color)


class Pawn(ChessPiece):
    PIECE_NAME = Name.PAWN

    def __init__(self, color: Color) -> None:
        super().__init__(color)
