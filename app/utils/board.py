from typing import Literal

from utils import (
    FILES,
    LABELED_BOARD,
    POSITION_IDX,
    RANKS,
    SQUARE_TYPE,
    STARTING_POSITION,
)
from utils.piece import Bishop, ChessPiece, Color, King, Knight, Name, Pawn, Queen, Rook
from utils.player import Player


class ChessBoard:
    def __init__(self) -> None:
        self.position: list[list[None | ChessPiece]] = [
            [None for _ in range(8)] for _ in range(8)  # type: ignore
        ]
        self.squares = LABELED_BOARD

    def get_index_of_square(
        self, square: SQUARE_TYPE
    ) -> dict[Literal["file", "rank"], int]:
        """
        Takes square (A1-H8)
        Returns list[int] pointing to specific board position
        NOTE: Base format is File + Rank | Position array requires indexing Rank prior to File
        """
        assert not square in LABELED_BOARD
        assert len(square) == 2

        rank = (7 - RANKS.index(square[1]))  # 7 for idx offset
        file = FILES.index(square[0])

        return {"file": file, "rank": rank}

    def _get_square_of_index(self, rank: POSITION_IDX, file: POSITION_IDX) -> str:
        """
        Takes list[2 idxs] (rank, file)
        Returns square (A1-H8)
        """
        square = LABELED_BOARD[rank][file]  # type: ignore

        return square

    # def populate_board(self, pieces: list[ChessPiece]):

    def setup(self):
        piece_type: Name
        positions_by_color: dict[Color, list[str]]
        color: Color
        positions: list[str]
        square: SQUARE_TYPE

        for piece_type, positions_by_color in STARTING_POSITION.items():
            for color, positions in positions_by_color.items():
                for square in positions: # type: ignore
                    sqr_idxs = self.get_index_of_square(square)

                    rank = sqr_idxs["rank"]  # type: ignore
                    file = sqr_idxs["file"]  # type: ignore

                    piece_cls = eval(piece_type.title())
                    new_piece: ChessPiece = piece_cls(color)

                    self.position[rank][file] = new_piece  # type: ignore

    def display(self):
        ...

    def move_piece(self):
        ...
