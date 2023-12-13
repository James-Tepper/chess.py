from __future__ import annotations

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

        # Positive value = White Advantage | Negative value = Black Advantage
        self.material_advantage: int = 0
        self.positional_advantage: float = 0.0

    def switch_turn(self):
        self.current_turn = (
            Color.WHITE if self.current_turn == Color.BLACK else Color.BLACK
        )

    def is_square_occupied(self, square: str) -> bool | ChessPiece:
        sqr_idxs = self.board.get_index_of_square(square)

        rank = sqr_idxs["rank"]  # type: ignore
        file = sqr_idxs["file"]  # type: ignore

        return self.position[rank][file] is not None  # type: ignore

    def is_square_occupied_by_oppenent(
        self, player: Player, square: str
    ) -> bool | ChessPiece:
        sqr_idxs = self.board.get_index_of_square(square)

        rank = sqr_idxs["rank"]  # type: ignore
        file = sqr_idxs["file"]  # type: ignore

        piece = self.board.position[rank][file] # type: ignore

        # TODO Maybe fix: Currently returns either Piece on specific square or True (meaning opp is on square)
        if not isinstance(piece, ChessPiece):
            return False
            # Returns Piece object if it's Player's own piece else TRUE -> refering to square is occupied

        return piece if not piece.color == square.color else True

    def check_for_checkmate(self):
        ...
