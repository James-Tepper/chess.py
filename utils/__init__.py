from __future__ import annotations

from typing import SupportsIndex


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

    def get_legal_moves(self, board_state, position):
        """
        Returns a list of legal moves for a piece at a given position.
        """
        # Check if king is directly hit by illegal move check()

        ...

    def is_within_board(self, position):
        row, col = position
        return 0 <= row < 8 and 0 <= col < 8

    def is_square_occupied(self, board_state, position):
        row, col = position
        return board_state[row][col] is not None

    def is_square_occupied_by_oppenent(self, board_state, position):
        row, col = position
        piece = board_state[row][col]  # TODO better variable name

        if piece is not None and not piece.color == self.color:
            return piece

        return None  # TODO fix?


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



ROW = ["1", "2", "3", "4", "5", "6", "7", "8"]
COLUMN = ["A", "B", "C", "D", "E", "F", "G", "H"]




# utils/board.py
class ChessBoard:
    def __init__(self) -> None:
        self.board: list[list[None | ChessPiece]] = [[None for _ in range(8)] for _ in range(8)]
        self.labeled_board = [[letter + number for number in ROW] for letter in COLUMN] #TODO Implement (reference will be offset by 1)

    def initialize_board(self):
        ...

    def display(self):
        ...

    def move_piece(self):
        ...


# utils/game.py
class Game:
    def __init__(self, whos_turn: Color = Color.WHITE) -> None:
        self.board = ChessBoard()
        self.current_turn = whos_turn

    def switch_turn(self):
        self.current_turn = (
            Color.BLACK if self.current_turn == Color.WHITE else Color.WHITE
        )

    def check_for_checkmate(self):
        ...


# class Piece:
#     def __init__(self, name: PieceName) -> None:
#         self.name = PieceName


class MoveHistory:
    ...
