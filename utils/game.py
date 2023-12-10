from __future__ import annotations

from utils.board import ChessBoard
from utils.piece import Color


# utils/game.py
class Game:
    def __init__(self, current_turn: Color = Color.WHITE) -> None:
        self.board = ChessBoard()
        self.current_turn = current_turn

    def switch_turn(self):
        self.current_turn = (
            Color.BLACK if self.current_turn == Color.WHITE else Color.WHITE
        )

    def check_for_checkmate(self):
        ...


class Player:
    def __init__(self, color: Color) -> None:
        self.turn = color == Color.WHITE
    def move(self):
        ... # TODO if self.turn MOVE.ENABLE


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
