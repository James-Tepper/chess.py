from __future__ import annotations

from typing import Dict, List, Literal, Tuple, cast

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
    StartingRank,
)


# Game class
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
        self.piece_types_on_board: Dict[PieceColor, List[PieceName]] = {
            PieceColor.WHITE: [
                PieceName.KING,
                PieceName.QUEEN,
                PieceName.ROOK,
                PieceName.BISHOP,
                PieceName.KNIGHT,
                PieceName.PAWN,
            ],
            PieceColor.BLACK: [
                PieceName.KING,
                PieceName.QUEEN,
                PieceName.ROOK,
                PieceName.BISHOP,
                PieceName.KNIGHT,
                PieceName.PAWN,
            ],
        }

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

    def can_castle_kingside(self, color):
        ...


    def can_castle_queenside(self, color):
        ...

    def get_legal_moves(self) -> Dict[PieceName, SQUARE_TYPE]: ...

    def get_legal_moves_for_piece(self, piece: ChessPiece): ...

    def switch_turn(self):
        self.current_turn = (
            PieceColor.WHITE
            if self.current_turn == PieceColor.BLACK
            else PieceColor.BLACK
        )

    def is_square_occupied(self, square: SQUARE_TYPE) -> bool | ChessPiece:
        sqr_idxs = self.board.get_index_of_square(square)

        rank = sqr_idxs["rank"]
        file = sqr_idxs["file"]

        return self.board.active_board[rank][file] is not None

    def is_square_occupied_by_oppenent(
        self, color: PieceColor, square: SQUARE_TYPE
    ) -> bool:
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
        return not piece.color == color

    def check_for_checkmate(self): ...


# Board classes
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

        assert isinstance(square_occupacy, ChessPiece)

        if square_occupacy.color == player.color:
            return SquareStatus.OCCUPIED_BY_OPPONENT_PIECE

        else:
            return SquareStatus.OCCUPIED_BY_OWN_PIECE


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


# Player Class
class Player:
    def __init__(
        self, color: Literal[PieceColor.WHITE, PieceColor.BLACK]
    ) -> None:  # TODO DO
        self.color = color
        self.move = Move(self.color)


# Move Class
# TODO reassess implemnation to allow for 1 instance (make more dynamic)
class Move:
    def __init__(self, color) -> None:
        self.color = color
        self.turn = True if self.color == PieceColor.WHITE else False

    # TODO __init__ method to dynamically generate moves at runtime
    def generate_valid_moves(self) -> List[Dict[ChessPiece, List[SQUARE_TYPE]]] | None:
        """
        Returns Square of piece

        """
        if not self.turn:
            # TODO implement turn rotation
            raise AttributeError("Didn't implement turn rotation")

        # self.get_king_moves()
        # self.get_queen_moves()
        # self.get_pawn_moves()
        # self.get_rook_moves()
        # self.get_knight_moves()
        # self.get_knight_moves()

    # def get_pawn_moves(board_state, position):
    #     ...

    # def get_rook_moves(board_state, position):
    #     ...

    # def get_knight_moves(board_state, position):
    #     ...

    # def get_bishop_moves(board_state, position):
    #     ...

    # def get_queen_moves(board_state, position):
    #     ...

    # def get_king_moves(board_state, position):
    #     ...

    # TODO add move rules
    def is_within_board(self, square: SQUARE_TYPE):
        file, rank = square

        return file in FILES and rank in RANKS

    def is_move_legal_for_piece(
        self,
        piece: ChessPiece,
        current_square: SQUARE_TYPE,
        target_square: SQUARE_TYPE,
        game: Game,
    ) -> bool:
        # Change bool ret to list maybe (or implement it on higher level)

        if piece not in game.piece_types_on_board[self.color]:
            return False

        current_file = FILES.index(current_square[0])
        current_rank = 7 - RANKS.index(current_square[1])

        target_file = FILES.index(target_square[0])
        target_rank = 7 - RANKS.index(target_square[1])

        match piece.PIECE_NAME:
            # SQUARE IS OCCUPIED (CAN ONLY MOVE UP AND OVER)
            case PieceName.PAWN:
                if self.turn == PieceColor.WHITE:
                    # Forward movement
                    if target_file == current_file:
                        if (
                            target_rank == current_rank + 1
                            and not game.is_square_occupied(square=target_square)
                        ):
                            return True

                        # Initial Double Movement
                        if (
                            current_rank == StartingRank.WHITE_PAWN
                            and target_rank == current_rank + 2
                        ):
                            intermediate_square = (
                                current_square[0],
                                RANKS[6 - (current_rank + 1)],
                            )
                            intermediate_square = cast(
                                SQUARE_TYPE, "".join(intermediate_square).upper()
                            )
                            if not game.is_square_occupied(
                                square=target_square
                            ) and not game.is_square_occupied(
                                square=intermediate_square
                            ):
                                return True

                    # Diagonal Capture
                    if (
                        abs(target_file - current_file) == 1
                        and target_file == current_rank + 1
                    ):
                        if game.is_square_occupied_by_oppenent(
                            square=target_square, color=piece.color
                        ):
                            return True

                elif self.turn == PieceColor.BLACK:
                    # Forward Movement
                    if target_file == current_file:
                        # TODO double check logic
                        if (
                            target_rank == current_rank - 1
                            and not game.is_square_occupied(square=target_square)
                        ):
                            return True

                        # Initial Double Movement
                        if (
                            current_rank == StartingRank.BLACK_PAWN
                            and target_rank == current_rank - 2
                        ):
                            # TODO CHECK LINE
                            intermediate_square = (
                                current_square[0],
                                RANKS[6 - (current_rank - 1)],
                            )
                            intermediate_square = cast(
                                SQUARE_TYPE, "".join(intermediate_square).upper()
                            )
                            if not game.is_square_occupied(
                                square=target_square
                            ) and not game.is_square_occupied(
                                square=intermediate_square
                            ):
                                return True
                    # Diagonal Capture
                    if (
                        abs(current_file - target_file) == 1
                        and target_file == current_rank - 1
                    ):
                        if game.is_square_occupied_by_oppenent(
                            square=target_square, color=piece.color
                        ):
                            return True

                else:
                    raise AssertionError("Issue with pawn functionality")

                    # return target_rank < current_rank

            case PieceName.KING:
                if abs(current_file - target_file) <= 1 and abs(current_rank - target_rank) <= 1:
                    if not game.is_square_occupied_by_oppenent(square=target_square, color=piece.color):
                        return True

                # Castling
                if piece.color == PieceColor.WHITE and current_square == "E1" and piece.has_moved == False:
                    if target_square == "G1" and game.can_castle_kingside(piece.color):
                        return True
                    if target_square == "C1" and game.can_castle_queenside(piece.color):
                        return True

                if piece.color == PieceColor.BLACK and current_square == "E8" and piece.had_moved == False:
                    if target_square == "G8" and game.can_castle_kingside(piece.color):
                        return True
                    if target_square == "C8" and game.can_castle_queenside(piece.color):
                        return True

                else:
                    return False

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

        if not self.is_move_legal_for_piece(piece, current_square, target_square, game):
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
        if not self.is_valid(game, piece, current_square, target_square):
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


# class Move:
#     def __init__(self) -> None:
#         ...

#     def validate(
#         self, player: Player, piece: ChessPiece, board: ChessBoard, current_square: SQUARE_TYPE
#     ):
#         curr_position = board.get_index_of_square(current_square)
#         curr_rank = curr_position["rank"]
#         curr_file = curr_position["file"]

#         # Check if the path to the position is clear
#         piece_position = board.position[curr_rank][curr_file]

#         # Get valid move from parent method
#         unfiltered_valid_moves = piece.get_valid_moves(self, board, current_square)

#         # TODO Filter out moves where the piece is pinned to the King

#         valid_moves = [
#             move
#             for move in unfiltered_valid_moves
#             if self.is_path_clear(board, piece_position, move)
#             and self.not_pinned_to_king(board, piece_position)
#         ]
#         return valid_moves

#     def is_check(self) -> bool:
#         ...

#     def not_pinned_to_king(self, piece: ChessPiece) -> bool:


#     def _check_if_legal(self) -> bool:
#         ...
#         """
#         Is king hit || will king be hit by movement of piece

#         """

#     def move_piece(self, curr_sqr: SQUARE_TYPE, new_sqr: SQUARE_TYPE):
#         # check_if_legal()
#         ...


# # TODO Implement checker if king is directly hit by move check(color)


# class MoveHistory:
#     def __init__(self) -> None:
#         self.history = {}


# # General Move Legality

# # def get_moves(board_state, position):
# #     ...


# def get_pawn_moves(board_state, position):
#     ...


# def get_rook_moves(board_state, position):
#     ...


# def get_knight_moves(board_state, position):
#     ...


# def get_bishop_moves(board_state, position):
#     ...


# def get_queen_moves(board_state, position):
#     ...


# def get_king_moves(board_state, position):
#     ...


# # Castling
# def can_castle(board_state, color, side):
#     ...


# def perform_castle(board_state, color, side):
#     ...


# # En Passant
# def can_en_passant(board_state, from_position, to_position):
#     ...


# def perform_en_passant(board_state, from_position, to_position):
#     ...


# # Pawn Promotion
# def can_promote_pawn(board_state, position):
#     ...


# def promote_pawn(board_state, position, new_piece):
#     ...
