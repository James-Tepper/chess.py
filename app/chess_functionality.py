from pydantic import BaseModel

from app.dtos.piece import PieceDTO
from app.utils import SQUARE_TYPE, PieceColor
from app.utils.board import ChessBoard
from app.chess_piece import ChessPiece
from app.utils.player import Player
from app.utils import ChessPiece

class MoveDTO(BaseModel):
    # TODO add move rules
    piece: PieceDTO
    target_square: SQUARE_TYPE

    def is_valid(self, game: Game) -> bool: ...

    def apply(self, game: Game): ...


class Game:
    def __init__(
        self,
    ) -> None:
        self.board = ChessBoard()
        self.current_player = PieceColor.WHITE
        self.legal_moves = self.get_legal_moves()
        self.in_check = {PieceColor.WHITE: False, PieceColor.BLACK: False}
        self.can_castle = {PieceColor.WHITE: True, PieceColor.BLACK: True}

        # Positive value = White Advantage | Negative value = Black Advantage
        self.material_advantage: int = 0
        self.positional_advantage: float = 0.0

    def get_legal_moves(self):
        ...

    def get_legal_moves_for_piece(self, piece: ChessPiece):
        ...

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


    def check_for_checkmate(self): ...
