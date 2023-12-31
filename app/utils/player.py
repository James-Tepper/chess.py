from utils import PieceColor
from utils.move import Move
from utils.game import Game
from typing import List

class Player:
    def __init__(self, color: PieceColor) -> None:
        self.color = color
        self.moves: List[Move] = []

    """
    def take(self):

    """

    def can_move(self, game: Game):
        # if self.color == game.current_turn:
        ...
