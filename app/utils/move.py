from utils import SQUARE_TYPE, PieceColor
from app.chess_functionality import ChessBoard
from app.chess_functionality import Game
from app.chess_piece import ChessPiece
from utils.player import Player

class Move:
    def __init__(self) -> None:
        ...

    def validate(
        self, player: Player, piece: ChessPiece, board: ChessBoard, current_square: SQUARE_TYPE
    ):
        curr_position = board.get_index_of_square(current_square)
        curr_rank = curr_position["rank"]
        curr_file = curr_position["file"]

        # Check if the path to the position is clear
        piece_position = board.position[curr_rank][curr_file]

        # Get valid move from parent method
        unfiltered_valid_moves = piece.get_valid_moves(self, board, current_square)

        # TODO Filter out moves where the piece is pinned to the King

        valid_moves = [
            move
            for move in unfiltered_valid_moves
            if self.is_path_clear(board, piece_position, move)
            and self.not_pinned_to_king(board, piece_position)
        ]
        return valid_moves

    def is_check(self) -> bool:
        ...

    def not_pinned_to_king(self, piece: ChessPiece) -> bool:



    def _check_if_legal(self) -> bool:
        ...
        """
        Is king hit || will king be hit by movement of piece

        """

    def move_piece(self, curr_sqr: SQUARE_TYPE, new_sqr: SQUARE_TYPE):
        # check_if_legal()
        ...


# TODO Implement checker if king is directly hit by move check(color)


class MoveHistory:
    def __init__(self) -> None:
        self.history = {}


# General Move Legality

# def get_moves(board_state, position):
#     ...


def get_pawn_moves(board_state, position):
    ...


def get_rook_moves(board_state, position):
    ...


def get_knight_moves(board_state, position):
    ...


def get_bishop_moves(board_state, position):
    ...


def get_queen_moves(board_state, position):
    ...


def get_king_moves(board_state, position):
    ...


# Castling
def can_castle(board_state, color, side):
    ...


def perform_castle(board_state, color, side):
    ...


# En Passant
def can_en_passant(board_state, from_position, to_position):
    ...


def perform_en_passant(board_state, from_position, to_position):
    ...


# Pawn Promotion
def can_promote_pawn(board_state, position):
    ...


def promote_pawn(board_state, position, new_piece):
    ...
