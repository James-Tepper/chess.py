from utils import COLUMN, ROW, LABELED_BOARD
from utils.piece import ChessPiece


class ChessBoard:
    def __init__(self) -> None:
        self.position: list[list[None | ChessPiece]] = [
            [None for _ in range(8)] for _ in range(8)  # type: ignore
        ]

    def format_board(self):
        """
        Used to convert self.position
        Into Chess Format
        """

    def initialize_board(self):
        for i in self.position:
            ...

    def display(self):
        ...

    def move_piece(self):
        ...


def initialize_board():
    ...


def display_board(board_state):
    ...
