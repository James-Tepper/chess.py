from __future__ import annotations

from typing import Dict, List, Literal, Tuple

from app.chess_piece import ChessPiece
from app.dtos.piece import PieceDTO
from app.utils.constants import (
    FILE_TYPE,
    FILES,
    LABELED_BOARD,
    POSITION_IDX,
    RANK_TYPE,
    RANKS,
    SQUARE_TYPE,
    STARTING_POSITION,
    ChessPiece,
    PieceColor,
    PieceName,
    PieceTypes,
    SquareStatus,
)


class Game:
    def __init__(
        self,
    ) -> None:
        self.board = ChessBoard()
        self.bit_board = BitBoard()
        self.current_turn = PieceColor.WHITE
        self.legal_moves = self.get_legal_moves()
        self.in_check = {PieceColor.WHITE: False, PieceColor.BLACK: False}
        self.king_moved = {PieceColor.WHITE: False, PieceColor.BLACK: False}
        # TODO implement way to check rook moved (for castling)

        # TODO can_castle 4 bools for each side
        self.can_castle = {PieceColor.WHITE: False, PieceColor.BLACK: False}

        # Positive value = White Advantage | Negative value = Black Advantage
        self.material_advantage: int = 0
        self.positional_advantage: float = 0.0

    def initialize_bitboard(self) -> None:
        self.piece_bitboards = {
            PieceName.PAWN: {
                PieceColor.WHITE: BitBoard(),
                PieceColor.BLACK: BitBoard(),
            },
            PieceName.ROOK: {
                PieceColor.WHITE: BitBoard(),
                PieceColor.BLACK: BitBoard(),
            },
            PieceName.KNIGHT: {
                PieceColor.WHITE: BitBoard(),
                PieceColor.BLACK: BitBoard(),
            },
            PieceName.BISHOP: {
                PieceColor.WHITE: BitBoard(),
                PieceColor.BLACK: BitBoard(),
            },
            PieceName.QUEEN: {
                PieceColor.WHITE: BitBoard(),
                PieceColor.BLACK: BitBoard(),
            },
            PieceName.KING: {
                PieceColor.WHITE: BitBoard(),
                PieceColor.BLACK: BitBoard(),
            },
        }

        piece_order: Tuple = (
            PieceName.ROOK,
            PieceName.KNIGHT,
            PieceName.BISHOP,
            PieceName.QUEEN,
            PieceName.KING,
            PieceName.BISHOP,
            PieceName.KNIGHT,
            PieceName.ROOK,
        )

        # Populating Pawns
        for file in range(8):

            curr_file = chr(file + ord("A")).upper()
            assert isinstance(curr_file, FILE_TYPE)

            self.piece_bitboards[PieceName.PAWN][PieceColor.WHITE].set_piece(
                BoardSquare(curr_file, "2")
            )
            self.piece_bitboards[PieceName.PAWN][PieceColor.BLACK].set_piece(
                BoardSquare(curr_file, "7")
            )

        # Populating Other Pieces
        for file, piece in enumerate(piece_order):

            curr_file = chr(file + ord("A")).upper()
            assert isinstance(curr_file, FILE_TYPE)

            self.piece_bitboards[piece][PieceColor.WHITE].set_piece(
                BoardSquare(curr_file, "1")
            )
            self.piece_bitboards[piece][PieceColor.BLACK].set_piece(
                BoardSquare(curr_file, "8")
            )

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

        return self.board.active_board[rank][file] is not None

    def _is_square_occupied_by_oppenent(
        self, player: Player, square: SQUARE_TYPE
    ) -> bool | ChessPiece:
        """
        T/F || Piece if belongs to player who's moving
        """
        sqr_idxs = self.board.get_index_of_square(square)

        rank = sqr_idxs["rank"]
        file = sqr_idxs["file"]

        piece = self.board.active_board[rank][file]

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
        self.file = ord(file.upper()) - ord("A")
        self.rank = int(rank) - 1

    def to_int(self) -> int:
        """
        Converts each board square to an integer between 0 and 63.
        The bottom left square (A1) maps to 0 and the top right square (H8) maps to 63.
        Mapping is incremented horizontally from left to right, bottom to top.
        """
        return (7 - self.rank) * 8 + self.file


class ChessBoard:
    def __init__(self) -> None:
        self.bit_board = BitBoard()
        self.active_board: List[List[None | ChessPiece]] = [
            [None for _ in range(8)] for _ in range(8)
        ]  # TODO refactor to replace with bitboard
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
                for square in positions:  # type:ignore
                    assert isinstance(square, SQUARE_TYPE)
                    if square[1] in ("3", "4", "5", "6"):
                        continue

                    sqr_idxs = self.get_index_of_square(square)
                    rank = sqr_idxs["rank"]
                    file = sqr_idxs["file"]

                    new_piece = PieceTypes[piece](color)

                    self.active_board[rank][file] = new_piece

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

        return self.active_board[rank][file] is not None

    def _is_the_square_occupied(
        self, player: Player, square: SQUARE_TYPE
    ) -> SquareStatus:
        """
        None if Player's Piece
        """

        """
        TODO check ret case in following function to retrieve piece info
        """

        sqr_idxs = self.get_index_of_square(square)

        rank = sqr_idxs["rank"]
        file = sqr_idxs["file"]

        square_occupacy = (
            self.active_board[rank][file]
            if isinstance(self.active_board[rank][file], ChessPiece)
            else SquareStatus.EMPTY
        )

        if not square_occupacy:
            return SquareStatus.EMPTY

        assert type(square_occupacy) is ChessPiece

        if square_occupacy.color == player.color:
            return SquareStatus.OCCUPIED_BY_OPPONENT_PIECE

        else:
            return SquareStatus.OCCUPIED_BY_OWN_PIECE


class Player:
    def __init__(
        self, color: Literal[PieceColor.WHITE, PieceColor.BLACK]
    ) -> None:  # TODO DO
        self.color = color


# TODO reassess implemnation to allow for 1 instance (make more dynamic)
class Move:
    # TODO __init__ method to dynamically generate moves at runtime
    # TODO add move rules
    def is_within_board(self, square: SQUARE_TYPE):
        file, rank = square

        return file in FILES and rank in RANKS

    def is_move_legal_for_piece(
        self, piece: ChessPiece, current_square: SQUARE_TYPE, target_square: SQUARE_TYPE
    ) -> bool:

        current_file = FILES.index(current_square[0])
        current_rank = 7 - RANKS.index(current_square[1])

        target_file = FILES.index(target_square[0])
        target_rank = 7 - RANKS.index(target_square[1])

        match piece.PIECE_NAME:
            case PieceName.PAWN:
                if piece.color == PieceColor.WHITE:
                    return target_rank > current_rank
                elif piece.color == PieceColor.BLACK:
                    return target_rank < current_rank
            case PieceName.KING:
                ...
            case PieceName.QUEEN:
                ...
            case PieceName.ROOK:
                ...
            case PieceName.BISHOP:
                ...
            case PieceName.KNIGHT:
                ...
            case _:
                raise AssertionError("Unkown Piece Type")

    # TODO finish method
    def is_valid(
        self,
        game: Game,
        piece: ChessPiece,
        current_square: SQUARE_TYPE,
        target_square: SQUARE_TYPE,
    ) -> bool:
        if not self.is_within_board(target_square):
            return False

        if not self.is_move_legal_for_piece(piece, current_square, target_square):
            return False

        return True

    def apply(
        self,
        game: Game,
        piece: ChessPiece,
        current_square: SQUARE_TYPE,
        target_square: SQUARE_TYPE,
    ):
        # update 'physical board'
        # update bitboard
        if not self.is_valid(game, current_square, target_square):
            return False
            #!!TODO implement is_valid checker for bitboard

        current_file = FILES.index(current_square[0])
        current_rank = 7 - RANKS.index(current_square[1])

        target_file = FILES.index(target_square[0])
        target_rank = 7 - RANKS.index(target_square[1])

        # Update active board
        game.board.active_board[target_rank][target_file] = piece

        # TODO maybe implement generator between active board and bitboard for more efficiency (probably not necessary)

        if target_rank not in RANKS or current_rank not in RANKS:
            return False

        if target_file not in FILES or current_file not in FILES:
            return False

        bit_board_target_square = BoardSquare(file=target_file, rank=target_rank)
        bit_board_current_square = BoardSquare(file=current_file, rank=current_rank)

        # Update bitboard
        game.board.bit_board.move_piece(
            current_square=bit_board_current_square, new_square=bit_board_target_square
        )

        if game.board.bit_board.is_square_occupied(bit_board_target_square):
            game.board.bit_board.remove_piece(bit_board_target_square)

        # TODO double check implementation
        game.board.bit_board.set_piece(bit_board_target_square)
