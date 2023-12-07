# General Movement
def move_piece(board_state, from_position, to_position):
    """
    Moves a piece from one position to another and updates the board state.
    """
    ...

# General Move Legality

# def get_moves(board_state, position):
#     """
#     Returns a list of legal moves for a piece at a given position.
#     """
#     ...


def is_move_legal(board_state, from_position, to_position) -> bool:
    """
    Determines if a move from one position to another is legal.
    """
    ...


def get_pawn_moves(board_state, position):
    """
    Returns legal moves for a pawn at the given position, including en passant.
    """
    ...


def get_rook_moves(board_state, position):
    """
    Returns legal moves for a rook at the given position.
    """
    ...


def get_knight_moves(board_state, position):
    """
    Returns legal moves for a knight at the given position.
    """
    ...


def get_bishop_moves(board_state, position):
    """
    Returns legal moves for a bishop at the given position.
    """
    ...


def get_queen_moves(board_state, position):
    """
    Returns legal moves for a queen at the given position.
    """
    ...


def get_king_moves(board_state, position):
    """
    Returns legal moves for a king at the given position, including castling.
    """
    ...


# Castling
def can_castle(board_state, color, side):
    """
    Checks if castling is possible for the given color and side (kingside or queenside).
    """
    ...


def perform_castle(board_state, color, side):
    """
    Performs the castling move.
    """
    ...


# En Passant
def can_en_passant(board_state, from_position, to_position):
    """
    Checks if en passant is possible for a given pawn move.
    """
    ...


def perform_en_passant(board_state, from_position, to_position):
    """
    Performs the en passant move.
    """
    ...


# Pawn Promotion
def can_promote_pawn(board_state, position):
    """
    Checks if a pawn is eligible for promotion.
    """
    ...


def promote_pawn(board_state, position, new_piece):
    """
    Promotes a pawn to the chosen new piece (queen, rook, bishop, knight).
    """
    ...
