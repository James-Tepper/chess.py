import setup
from utils.game import Game
from utils import LABELED_BOARD


def main():
    game_state = Game()
    
    # Currently empty
    board = game_state.board
    board.setup()
    board.get_square_of_index(rank=0, file=0)
    

if "__main__" == __name__:
    main()


