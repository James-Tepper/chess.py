from utils import Color
from utils.move import Move

class Player:
    def __init__(self, color: Color) -> None:
        self.color = color
        self.move = Move()
    
    """
    def take(self):
        
    """

    def can_move(self):
        ...  # TODO if self.turn MOVE.ENABLE
