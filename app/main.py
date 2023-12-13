import setup
from utils.game import Game
from utils import LABELED_BOARD


def main():
    game_state = Game()
    empty_board = game_state.board
    # pieces = setup.create_pieces()

    empty_board.populate_board()

if "__main__" == __name__:
    main()


