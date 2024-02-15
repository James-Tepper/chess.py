import base64
from enum import IntEnum
from pydantic import BaseModel
from typing import List

class PieceType(IntEnum):
    PAWN = 1
    KNIGHT = 2
    BISHOP = 3
    ROOK = 4
    QUEEN = 5
    KING = 6


class PieceColor(IntEnum):
    WHITE = 0
    BLACK = 1


class PieceStatus(IntEnum):
    OFF_BOARD = 0
    ON_BOARD = 1

# maybe check status first?
class PieceDTO(BaseModel):
    piece_type: PieceType
    color: PieceColor
    status: PieceStatus
    rank: int  # TODO prob create way to convert
    file: int
    extra: int

    def encode_piece(self) -> bytearray:
        byte = (
            (self.piece_type.value & 0b111)
            | ((self.color.value & 0b1) << 3)
            | ((self.status & 0b1) << 4)
            | ((self.rank & 0b1111) << 5)
            | ((self.file & 0b1111) << 9)
            | ((self.extra & 0b1) << 15)
        )
        return bytearray([byte & 0xFF, (byte >> 8) & 0xFF])

    @classmethod #type: ignore
    def decode_piece(cls, byte: bytearray):
        value = byte[0] | (byte[1] << 8)
        piece_type_value = value & 0b111
        color_value = (value >> 3) & 0b1
        status = (value >> 4) & 0b1
        rank = (value >> 5) & 0b1111
        file = (value >> 9) & 0b1111
        extra = (value >> 15) & 0b1

        piece_type = PieceType(piece_type_value)
        color = PieceColor(color_value)

        return cls(
            piece_type=piece_type,
            color=color,
            status=status,
            rank=rank,
            file=file,
            extra=extra,
        )


def encode_piece_for_network(piece: PieceDTO) -> str:
    encoded_piece = piece.encode_piece()
    return base64.b64encode(encoded_piece).decode("utf-8")


def encode_pieces_for_network(pieces: List[PieceDTO]) -> List[str]:
    return [encode_piece_for_network(piece) for piece in pieces]


def filter_pieces_on_board(pieces: List[PieceDTO]) -> List[PieceDTO]:
    return [piece for piece in pieces if piece.status == PieceStatus.ON_BOARD]


def parse_encoded_pieces(encoded_pieces: str) -> List[PieceDTO]:
    encoded_pieces_list = encoded_pieces.split(",")

    return [PieceDTO.decode_piece(encoded_piece) for encoded_piece in encoded_pieces_list]
