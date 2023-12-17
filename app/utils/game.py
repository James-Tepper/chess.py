from __future__ import annotations

from utils import SQUARE_TYPE
from utils.board import ChessBoard
from utils.piece import ChessPiece, Color
from utils.player import Player


# utils/game.py
class Game:
    def __init__(self, current_turn: Color = Color.WHITE) -> None:
        self.board = ChessBoard()
        self.current_turn = current_turn
        self.players = {
            Color.WHITE: Player(Color.WHITE),
            Color.BLACK: Player(Color.BLACK),
        }
        self.winner: Color | None = None

        # Positive value = White Advantage | Negative value = Black Advantage
        self.material_advantage: int = 0
        self.positional_advantage: float = 0.0

    def switch_turn(self):
        self.current_turn = (
            Color.WHITE if self.current_turn == Color.BLACK else Color.BLACK
        )


    def _is_square_occupied(self, square: SQUARE_TYPE) -> bool | ChessPiece:
        sqr_idxs = self.board.get_index_of_square(square)

        rank = sqr_idxs["rank"]
        file = sqr_idxs["file"]

        return self.position[rank][file] is not None

    def _is_square_occupied_by_oppenent(
        self, player: Player, square: SQUARE_TYPE
    ) -> bool | ChessPiece:
        """
        T/F || Piece if belongs to player who's moving
        """
        sqr_idxs = self.board.get_index_of_square(square)

        rank = sqr_idxs["rank"]
        file = sqr_idxs["file"]

        piece = self.board.position[rank][file]

        # TODO Maybe fix: Currently returns either Piece on specific square or True (meaning opp is on square)
        if not isinstance(piece, ChessPiece):
            return False
            # Returns Piece object if it's Player's own piece else TRUE -> refering to square is occupied
        return piece if not piece.color == player.color else True

    def check_for_checkmate(self):
        ...
