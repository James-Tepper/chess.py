from utils import FILES, LABELED_BOARD, RANKS, SQUARE_TYPE
from utils.game import Game
from utils.move import Move
from utils.piece import Color


def main():
    game_state = Game()

    # Board Configuration
    board = game_state.board
    board.setup()

    # Game loop
    while game_state.winner is None:
        whos_turn = (
            Color.WHITE if game_state.current_turn == Color.WHITE else Color.BLACK
        )

        selected_sqr = input("Select Piece: ").upper()
        new_sqr = input("Select Destination: ")
        if not len(selected_sqr) == 2:
            continue

        if not selected_sqr[0] in FILES or not selected_sqr[1] in RANKS:
            continue

        game_state.players[whos_turn]


if "__main__" == __name__:
    main()
