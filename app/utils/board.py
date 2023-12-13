from typing import Literal

from utils import FILES, LABELED_BOARD, POSITION_IDX, RANKS, STARTING_POSITION
from utils.piece import Bishop, ChessPiece, Color, King, Knight, Name, Pawn, Queen, Rook


class ChessBoard:
    def __init__(self) -> None:
        self.position: list[list[None | ChessPiece]] = [
            [None for _ in range(8)] for _ in range(8)  # type: ignore
        ]
        self.squares = LABELED_BOARD

    def get_index_of_square(self, square: str) -> list[int]:
        """
        Takes square (A1-H8)
        Returns list[int] pointing to specific board position
        NOTE: Base format is File + Rank | Position array requires indexing Rank prior to File
        """
        assert not square in LABELED_BOARD

        if not len(square) == 2:
            raise ValueError("Square can only be 2 characters")

        rank = 7 - RANKS.index(square[1])  # 7 for idx offset
        file = FILES.index(square[0])

        return [file, rank]

    def get_square_of_index(self, rank: POSITION_IDX, file: POSITION_IDX) -> str:
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
        square: str

        for piece_type, positions_by_color in STARTING_POSITION.items():
            for color, positions in positions_by_color.items():
                for square in positions:
                    sqr_idxs = self.get_index_of_square(square=square)

                    rank = sqr_idxs[1]  # type: ignore
                    file = sqr_idxs[0]  # type: ignore

                    piece_class_name = eval(piece_type.title())
                    new_piece: ChessPiece = piece_class_name(color=color)

                    self.position[rank][file] = new_piece

    def is_square_occupied(self, square) -> bool | ChessPiece:
        row, col = square
        return self.position[row][col] is not None

    def is_square_occupied_by_oppenent(self, square) -> bool | ChessPiece:
        row, col = square

        piece = self.position[row][col]  # TODO better variable name

        # TODO Maybe fix: Currently returns either Piece on specific square or True (meaning opp is on square)
        if not isinstance(piece, ChessPiece):
            return False
            # Returns Piece object if it's Player's own piece else TRUE -> refering to square is occupied

        return piece if not piece.color == square.color else True

    def display(self):
        ...

    def move_piece(self):
        ...
