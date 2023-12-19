from __future__ import annotations

from utils import SQUARE_TYPE, PieceColor
from utils.board import ChessBoard
from utils.piece import ChessPiece
from utils.player import Player


# utils/game.py
class Game:
    def __init__(
        self, board: ChessBoard, current_turn: PieceColor = PieceColor.WHITE
    ) -> None:
        self.board = board
        self.current_turn = current_turn
        self.players = {
            PieceColor.WHITE: Player(PieceColor.WHITE),
            PieceColor.BLACK: Player(PieceColor.BLACK),
        }
        self.winner: PieceColor | None = None

        # Positive value = White Advantage | Negative value = Black Advantage
        self.material_advantage: int = 0
        self.positional_advantage: float = 0.0

    def switch_turn(self):
        self.current_turn = (
            PieceColor.WHITE
            if self.current_turn == PieceColor.BLACK
            else PieceColor.BLACK
        )

    def _is_square_occupied(self, square: SQUARE_TYPE) -> bool | ChessPiece:
        sqr_idxs = self.board.get_index_of_square(square)

        rank = sqr_idxs["rank"]
        file = sqr_idxs["file"]

        return self.board.position[rank][file] is not None

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
