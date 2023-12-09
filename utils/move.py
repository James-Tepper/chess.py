# General Movement
def move_piece(board_state, from_position, to_position):
    ...

# General Move Legality

# def get_moves(board_state, position):
#     ...


def is_move_legal(board_state, from_position, to_position) -> bool:
    ...


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
