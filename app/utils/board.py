from typing import Literal

from utils import (
    FILES,
    RANKS,
    LABELED_BOARD,
    STARTING_POSITION,
)

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
        Returns int pointing to specific board position
        NOTE: Base format is File + Rank but position array requires indexing Rank prior to File
        """
        assert not square in LABELED_BOARD

        if not len(square) == 2:
            raise ValueError("Square can only be 2 characters")

        rank = RANKS.index(square[1])
        file = FILES.index(square[0])

        return [rank, file]

        # self.squares.index(square)

    def get_square_of_index(self, idx: list[int]) -> str:
        ...

    # def populate_board(self, pieces: list[ChessPiece]):
    def populate_board(self):
        piece_type: Name
        positions_by_color: dict[Color, list[str]]
        color: Color
        positions: list[str]
        position: str

        for piece_type, positions_by_color in STARTING_POSITION.items():
            for color, positions in positions_by_color.items():
                for position in positions:
                    piece_class_name = eval(piece_type.title())
                    new_piece = piece_class_name(color=color)

                    sqr_idxs = self.get_index_of_square(square=position)
                    
                    rank = sqr_idxs[0]
                    file = sqr_idxs[1]

                    self.position[rank][file] = new_piece
                    

                    #                     print(f'''
                    # piece_type= KING
                    # positions_by_color= <Color.WHITE: 'WHITE'>: ['E1'], <Color.BLACK: 'BLACK'>: ['E8']
                    # color= WHITE
                    # positions= ['E1']
                    # position= E1
                    #                           ''')


    def is_square_occupied(self, square) -> bool | ChessPiece:
        row, col = square
        return self.position[row][col] is not None

    def is_square_occupied_by_oppenent(self, square) -> bool | ChessPiece:
        row, col = square

        piece = self.position[row][col]  # TODO better variable name

        # TODO Maybe fix: Currently returns either Piece on specific square or True (meaning opp is on square)
        if isinstance(piece, ChessPiece):
            return piece if not piece.color == square.color else True
            # Returns Piece object if it's Player's own piece else TRUE -> refering to square is occupied

        return False

    def display(self):
        ...

    def move_piece(self):
        ...


def display_board(board_state):
    ...
