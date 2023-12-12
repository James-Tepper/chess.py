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
    def __init__(self, color: Color, name: Name) -> None:
        self.color = color
        self.name = name
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
        super().__init__(color, name=Name.KING)


class Queen(ChessPiece):
    def __init__(self, color: Color) -> None:
        super().__init__(color, name=Name.QUEEN)


class Rook(ChessPiece):
    def __init__(self, color: Color) -> None:
        super().__init__(color, name=Name.ROOK)


class Bishop(ChessPiece):
    def __init__(self, color: Color) -> None:
        super().__init__(color, name=Name.BISHOP)


class Knight(ChessPiece):
    def __init__(self, color: Color) -> None:
        super().__init__(color, name=Name.KNIGHT)


class Pawn(ChessPiece):
    def __init__(self, color: Color) -> None:
        super().__init__(color, name=Name.PAWN)
