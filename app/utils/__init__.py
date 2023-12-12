from piece import Color, Name

ROW = ["1", "2", "3", "4", "5", "6", "7", "8"]
COLUMN = ["A", "B", "C", "D", "E", "F", "G", "H"]


STARTING_POSITION: dict[Name, dict[Color, list[str]]] = {
    Name.KING: {Color.WHITE: ["E1"], Color.BLACK: ["E8"]},
    Name.QUEEN: {Color.WHITE: ["D1"], Color.BLACK: ["D8"]},
    Name.ROOK: {Color.WHITE: ["A1", "H1"], Color.BLACK: ["A8", "H8"]},
    Name.BISHOP: {Color.WHITE: ["C1", "F1"], Color.BLACK: ["C8", "F8"]},
    Name.KNIGHT: {Color.WHITE: ["B1", "G1"], Color.BLACK: ["B8", "G8"]},
    Name.PAWN: {
        Color.WHITE: ["A2", "B2", "C2", "D2", "E2", "F2", "G2", "H2"],
        Color.BLACK: ["A2", "B7", "C7", "D7", "E7", "F7", "G7", "H7"],
    },
}


LABELED_BOARD: list[list[str]] = [
    [letter + number for letter in COLUMN] for number in ROW[::-1]
]





print(LABELED_BOARD)

"""
[
idx 0    [(0,0), (0,1), (0,2), (0,3), (0,4), (0,5), (0,6), (0,7)],
idx 1    [(1,0), (1,1), (1,2), (1,3), (1,4), (1,5), (1,6), (1,7)],
idx 2    [(2,0), (2,1), (2,2), (2,3), (2,4), (2,5), (2,6), (2,7)],
idx 3    [(3,0), (3,1), (3,2), (3,3), (3,4), (3,5), (3,6), (3,7)],
idx 4    [(4,0), (4,1), (4,2), (4,3), (4,4), (4,5), (4,6), (4,7)],
idx 5    [(5,0), (5,1), (5,2), (5,3), (5,4), (5,5), (5,6), (5,7)],
idx 6    [(6,0), (6,1), (6,2), (6,3), (6,4), (6,5), (6,6), (6,7)],
idx 7    [(7,0), (7,1), (7,2), (7,3), (7,4), (7,5), (7,6), (7,7)],
]

FLIP 180

[
idx 7    [A8, B8, C8, D8, E8, F8, G8, H8],
idx 6    [A8, B8, C8, D8, E8, F8, G8, H8],
idx 5    [A8, B8, C8, D8, E8, F8, G8, H8],
idx 4    [A8, B8, C8, D8, E8, F8, G8, H8],
idx 3    [A8, B8, C8, D8, E8, F8, G8, H8],
idx 2    [A8, B8, C8, D8, E8, F8, G8, H8],
idx 1    [A1, B1, C1, D1, E1, F1, G1, H1],
idx 0    [A8, B8, C8, D8, E8, F8, G8, H8],
]


"""
