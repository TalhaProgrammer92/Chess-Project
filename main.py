from board.board import Board
from pieces.handler import PieceHandler
from logic.game import *
from player.player import *
import utils.settings as settings

if __name__ == '__main__':
    board: Board = Board()
    ph: PieceHandler = PieceHandler()
    ph.reset()

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

    game: Game = Game(board=board, piece_handler=ph, players=players)
    game.start_game()
