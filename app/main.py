import setup
from utils.game import Game


def main():
    game_state = Game()
    empty_board = game_state.board
    # pieces = setup.create_pieces()

    board = empty_board.populate_board()
    print(board)

if "__main__" == __name__:
    main()


'''

[
WHITE
idx=0    [],
idx=1    [],
idx=2    [],
idx=3    [],
idx=4    [],
idx=5    [],
idx=6    [],
idx=7    [],
BLACK
]

'''
