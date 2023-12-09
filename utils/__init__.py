from __future__ import annotations

from enum import StrEnum
from typing import SupportsIndex

from utils.enums import Color, Name


class ChessPiece:
    def __init__(self, color: Color, name: Name) -> None:
        self.color = color
        self.name = name

        if not name == Name.KNIGHT:
            self.abrev = str(color[0:1] + name[0:1]).upper()
        else:
            self.abrev = str(color[0:1] + "N").upper()


    # def check_if_valid_move(self, board_state, position):
    #     # Check if king is directly hit by move check(color)
    #     ...

    def is_within_board(self, position):
        row, col = position
        return 0 <= row < 7 and 0 <= col < 7

    # TODO Make 'position' for 'selected piece'
    def is_square_occupied(self, board_state: ChessBoard, position) -> bool | ChessPiece:
        row, col = position
        return board_state.curr_position[row][col] is not None

    def is_square_occupied_by_oppenent(
        self, board_state: ChessBoard, position
    ) -> bool | ChessPiece:
        row, col = position

        piece = board_state.curr_position[row][col]  # TODO better variable name

        # TODO Maybe fix: Currently returns either Piece on specific square or True (meaning opp is on square)
        if piece:
            piece: ChessPiece
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


ROW = ["1", "2", "3", "4", "5", "6", "7", "8"]
COLUMN = ["A", "B", "C", "D", "E", "F", "G", "H"]


# utils/board.py
class ChessBoard:
    def __init__(self) -> None:
        self.curr_position: list[list[None | ChessPiece]] = [
            [None for _ in range(8)] for _ in range(8)
        ]
        self.labeled_board = [
            [letter + number for number in ROW] for letter in COLUMN
        ]  # TODO Implement (reference will be offset by 1)

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


class Player:
    def __init__(self, color: Color) -> None:
        self.turn = color == Color.WHITE


class Move(Player):
    def check_if_valid_move(self, board_state, position):
        ...


# TODO Implement checker if king is directly hit by move check(color)

# class Piece:
#     def __init__(self, name: PieceName) -> None:
#         self.name = PieceName


class MoveHistory:
    def __init__(self) -> None:
        ...
