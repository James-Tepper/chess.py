from enum import IntEnum
from typing import Dict, cast

from dtos.piece import PieceColor, PieceDTO, PieceStatus, PieceType

# app/dtos/piece.py for details


def encode_piece(
    piece_type: PieceType,
    color: PieceColor,
    status: PieceStatus,
    rank: int,
    file: int,
    extra: int,
) -> bytearray:
    byte = (
        (piece_type.value & 0b111)
        | ((color.value & 0b1) << 3)
        | ((status & 0b1) << 4)
        | ((rank & 0b1111) << 5)
        | ((file & 0b1111) << 9)
        | ((extra & 0b1) << 15)
    )
    return bytearray([byte & 0xFF, (byte >> 8) & 0xFF])


def decode_piece(byte: bytearray) -> PieceDTO:
    value = byte[0] | (byte[1] << 8)
    piece_type_value = value & 0b111
    color_value = (value >> 3) & 0b1
    status = (value >> 4) & 0b1
    rank = (value >> 5) & 0b1111
    file = (value >> 9) & 0b1111
    extra = (value >> 15) & 0b1

    piece = PieceType(piece_type_value)
    color = PieceColor(color_value)

    return PieceDTO(
        piece_type=piece, color=color, status=status, rank=rank, file=file, extra=extra
    )
