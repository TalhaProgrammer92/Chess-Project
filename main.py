from board.board import Board
from pieces.handler import PieceHandler
from logic.game import *
from player.player import *
from data.csv_handler import *
import utils.settings as settings

if __name__ == '__main__':
    ph: PieceHandler = PieceHandler()
    ph.reset()
    board: Board = Board(ph)

    # board.place_pieces(ph.pieces)
    # board.display()

    # print(
    #     '',
    #     settings.message['error']['wrong-position'],
    #     settings.message['error']['empty-name'],
    #     settings.message['error']['wrong-entry'],
    #     sep='\n'
    # )

    players: list[Player] = [
        Player(name='Talha Ahmad', group='white'),
        Player(name='Rayan Zulfiqar', group='black')
    ]

    game: Game = Game(board=board, players=players)
    # game.start_game()

    save_game(game, 'slot-1')

    print('Saved Successfully!')
