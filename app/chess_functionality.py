from __future__ import annotations

from typing import Dict, List, Literal

from utils import (
    FILE_TYPE,
    FILES,
    LABELED_BOARD,
    POSITION_IDX,
    RANK_TYPE,
    RANKS,
    SQUARE_TYPE,
    STARTING_POSITION,
    PieceColor,
    PieceName,
    PieceTypes,
)

from app.chess_piece import ChessPiece
from app.dtos.piece import PieceDTO
from app.utils import SQUARE_TYPE, ChessPiece, PieceColor


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

    def get_legal_moves(self) -> Dict[PieceName, SQUARE_TYPE]: ...

    def get_legal_moves_for_piece(self, piece: ChessPiece): ...

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


class BitBoard:
    def __init__(self) -> None:
        self.b_board = 0

    def set_piece(self, square: BoardSquare) -> None:
        position = square.to_int()
        self.b_board |= 1 << position

    def remove_piece(self, square: BoardSquare) -> None:
        position = square.to_int()
        self.b_board &= ~(1 << position)

    def move_piece(self, current_square: BoardSquare, new_square: BoardSquare):
        self.remove_piece(current_square)
        self.set_piece(new_square)

    def is_square_occupied(self, square: BoardSquare):
        position = square.to_int()
        return (self.b_board & (1 << position)) != 0


class BoardSquare:
    def __init__(self, file: FILE_TYPE, rank: RANK_TYPE) -> None:
        self.file = file
        self.rank = rank

    def to_int(self) -> int:
        file_num = ord(self.file) - ord("A")
        rank_num = int(self.rank) - 1

        return rank_num * 8 + file_num


class ChessBoard:
    def __init__(self) -> None:
        self.position: List[List[None | ChessPiece]] = [
            [None for _ in range(8)] for _ in range(8)
        ]
        self.squares = LABELED_BOARD

        # Seeds board with starting position
        self.setup()

    def setup(self) -> None:
        piece: PieceName
        positions_by_color: Dict[PieceColor, List[str]]
        color: PieceColor
        positions: List[str]
        square: SQUARE_TYPE

        for piece, positions_by_color in STARTING_POSITION.items():
            for color, positions in positions_by_color.items():
                for square in positions:
                    if square[1] in ("3", "4", "5", "6"):
                        continue

                    sqr_idxs = self.get_index_of_square(square)
                    rank = sqr_idxs["rank"]
                    file = sqr_idxs["file"]

                    new_piece = PieceTypes[piece](color)

                    self.position[rank][file] = new_piece

    def get_index_of_square(
        self, square: SQUARE_TYPE
    ) -> Dict[Literal["file", "rank"], int]:
        """
        Takes square (A1-H8)
        Returns List[int] pointing to specific board position
        NOTE: Base format is File + Rank | Position array requires indexing Rank prior to File
        """
        rank = 7 - RANKS.index(square[1])  # 7 for idx offset
        file = FILES.index(square[0])

        return {"file": file, "rank": rank}

    # NOT NECESSARY
    def _get_square_of_index(self, rank: POSITION_IDX, file: POSITION_IDX) -> str:
        """
        Takes List[2 idxs] (rank, file)
        Returns square (A1-H8)
        """
        square = self.squares[rank][file]
        return square

    def _is_square_occupied(self, square: SQUARE_TYPE) -> bool | ChessPiece:
        sqr_idxs = self.get_index_of_square(square)

        rank = sqr_idxs["rank"]
        file = sqr_idxs["file"]

        return self.position[rank][file] is not None

    def _is_square_occupied_by_oppenent(
        self, player: Player, square: SQUARE_TYPE
    ) -> bool | ChessPiece:
        """
        T/F or Piece if belongs to player who's moving
        """
        sqr_idxs = self.get_index_of_square(square)

        rank = sqr_idxs["rank"]
        file = sqr_idxs["file"]

        piece = self.position[rank][file]

        # TODO Maybe fix: Currently returns either Piece on specific square or True (meaning opp is on square)
        if not isinstance(piece, ChessPiece):
            return False
            # Returns Piece object if it's Player's own piece else TRUE -> refering to square is occupied
        return piece if not piece.color == player.color else True


class Player:
    def __init__(
        self, color: Literal[PieceColor.WHITE, PieceColor.BLACK]
    ) -> None:  # TODO DO
        self.color = color


class Move:
    # TODO add move rules
    piece: PieceDTO
    target_square: SQUARE_TYPE

    def is_valid(self, game: Game) -> bool: ...

    def apply(self, game: Game): ...
