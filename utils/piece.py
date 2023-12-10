from __future__ import annotations

from utils.board import ChessBoard


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

    # TODO Make 'position' for 'selected piece'
    def is_square_occupied(
        self, board_state: ChessBoard, position
    ) -> bool | ChessPiece:
        row, col = position
        return board_state.curr_position[row][col] is not None

    def is_square_occupied_by_oppenent(
        self, board_state: ChessBoard, position
    ) -> bool | ChessPiece:
        row, col = position

        piece = board_state.curr_position[row][col]  # TODO better variable name

        # TODO Maybe fix: Currently returns either Piece on specific square or True (meaning opp is on square)
        if isinstance(piece, ChessPiece):
            return piece if not piece.color == self.color else True
            # Returns Piece object if it's Player's own piece else TRUE -> refering to square is occupied

        return False


class King(ChessPiece):
    def __init__(self, color: Color, name: Name) -> None:
        super().__init__(color, name)


class Queen(ChessPiece):
    def __init__(self, color: Color, name: Name) -> None:
        super().__init__(color, name)


class Rook(ChessPiece):
    def __init__(self, color: Color, name: Name) -> None:
        super().__init__(color, name)


class Bishop(ChessPiece):
    def __init__(self, color: Color, name: Name) -> None:
        super().__init__(color, name)


class Knight(ChessPiece):
    def __init__(self, color: Color, name: Name) -> None:
        super().__init__(color, name)


class Pawn(ChessPiece):
    def __init__(self, color: Color, name: Name) -> None:
        super().__init__(color, name)
