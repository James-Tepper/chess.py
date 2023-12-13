import setup
from utils.game import Game
from utils import LABELED_BOARD


def main():
    game_state = Game()
    
    # Currently empty
    board = game_state.board
    board.setup()
    # board._get_square_of_index(rank=0, file=0)
    # print(LABELED_BOARD)
    board.get_index_of_square("H1")

if "__main__" == __name__:
    main()


