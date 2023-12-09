
# TODO Implement later
def generate_board():
    with open("output.txt", 'w+') as f:
        print("board", file=f)


from utils import ChessPiece, Color, Name

class NameAbrev:
    '''
    Color: W = WHITE | B = BLACK
    NOTE: KING = K so KNIGHT = N
    '''
    # BLACK
    BK = ChessPiece(color=Color.BLACK, name=Name.KING)
    BQ = ChessPiece(color=Color.BLACK, name=Name.QUEEN)
    BR = ChessPiece(color=Color.BLACK, name=Name.ROOK)
    BB = ChessPiece(color=Color.BLACK, name=Name.BISHOP)
    BN = ChessPiece(color=Color.BLACK, name=Name.KNIGHT)
    BP = ChessPiece(color=Color.WHITE, name=Name.PAWN)
    
    # WHITE
    WK = ChessPiece(color=Color.BLACK, name=Name.KING)
    WQ = ChessPiece(color=Color.BLACK, name=Name.QUEEN)
    WR = ChessPiece(color=Color.BLACK, name=Name.ROOK)
    WB = ChessPiece(color=Color.BLACK, name=Name.BISHOP)
    WN = ChessPiece(color=Color.BLACK, name=Name.KNIGHT)
    WP = ChessPiece(color=Color.WHITE, name=Name.PAWN)



default_board = {
    "8": {"A": None, "B": None, "C": None, "D": None, "E": None, "F": None, "G": None, "H": None},
    "7": {"A": NameAbrev.BP, "B": NameAbrev.BP, "C": NameAbrev.BP, "D": NameAbrev.BP, "E": NameAbrev.BP, "F": NameAbrev.BP, "G": NameAbrev.BP, "H": NameAbrev.BP},
    "6": {"A": None, "B": None, "C": None, "D": None, "E": None, "F": None, "G": None, "H": None},
    "5": {"A": None, "B": None, "C": None, "D": None, "E": None, "F": None, "G": None, "H": None},
    "4": {"A": None, "B": None, "C": None, "D": None, "E": None, "F": None, "G": None, "H": None},
    "3": {"A": None, "B": None, "C": None, "D": None, "E": None, "F": None, "G": None, "H": None},
    "2": {"A": None, "B": None, "C": None, "D": None, "E": None, "F": None, "G": None, "H": None},
    "1": {"A": None, "B": None, "C": None, "D": None, "E": None, "F": None, "G": None, "H": None},
}

