import pytest
from chess_functionality import Game, ChessPiece, PieceColor, PieceName, BoardSquare


class TestGame:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.test_game = Game()

    def pawn_move(self):
        pawn = ChessPiece(PieceName.PAWN, PieceColor.WHITE)
        start_square = BoardSquare("A", "2")
        end_square = BoardSquare("A", "3")
