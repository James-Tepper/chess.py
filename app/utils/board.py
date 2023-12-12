from utils import COLUMN, ROW, LABELED_BOARD, STARTING_POSITION
from utils.piece import ChessPiece, Color, Name


class ChessBoard:
    def __init__(self) -> None:
        self.position: list[list[None | ChessPiece]] = [
            [None for _ in range(8)] for _ in range(8) # type: ignore
        ]

    def format_board(self):
        """
        Used to convert self.position
        Into Chess Format
        """
        '''
    [0,0] A8  [0,7] H8
        
        
    [7,0] A1  [7,7] H1
        '''

    # def populate_board(self, pieces: list[ChessPiece]):
    def populate_board(self):
        
        for piece, count in STARTING_POSITION.items():
            for idx, _ in enumerate(self.position):
                print(piece, count)
                if idx == 1:
                    ...                
                    # TODO Make 'position' for 'selected piece'

    def is_square_occupied(
        self, square
    ) -> bool | ChessPiece:
        row, col = square
        return self.position[row][col] is not None

    def is_square_occupied_by_oppenent(
        self, square
    ) -> bool | ChessPiece:
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
