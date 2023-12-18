from utils import SQUARE_TYPE, Color
from utils.game import Game
from utils.piece import ChessPiece


class Move:
    def __init__(self) -> None:
        ...

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
