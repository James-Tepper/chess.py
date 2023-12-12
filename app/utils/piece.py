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
    def __init__(self, name: Name, color: Color) -> None:
        self.name = name
        self.color = color
        self.abrev: str

        piece_abrev = name[0:1] if not name == Name.KNIGHT else "N"
        self.abrev = str(color[0:1] + piece_abrev).upper()

    # def check_if_valid_move(self, board_state, position):
    #     # Check if king is directly hit by move check(color)
    #     ...

    def is_within_board(self, position):
        row, col = position
        return 0 <= row < 7 and 0 <= col < 7


class King(ChessPiece):
    def __init__(self, color: Color) -> None:
        super().__init__(Name.KING, color)


class Queen(ChessPiece):
    def __init__(self, color: Color) -> None:
        super().__init__(Name.QUEEN, color)


class Rook(ChessPiece):
    def __init__(self, color: Color) -> None:
        super().__init__(Name.ROOK, color)


class Bishop(ChessPiece):
    def __init__(self, color: Color) -> None:
        super().__init__(Name.BISHOP, color)


class Knight(ChessPiece):
    def __init__(self, color: Color) -> None:
        super().__init__(Name.KNIGHT, color)


class Pawn(ChessPiece):
    def __init__(self, color: Color) -> None:
        super().__init__(Name.PAWN, color)
