from board.board import Board
from pieces.handler import PieceHandler
from logic.game import *
from player.player import *
# from data.csv_handler import *
import utils.settings as settings

if __name__ == '__main__':
    pieces: PieceHandler = PieceHandler()
    pieces.reset()

    board: Board = Board(pieces)

    players: list[Player] = [
        Player(name='Talha Ahmad', group='white'),
        Player(name='Rayan Zulfiqar', group='black')
    ]

    game: Game = Game(
        board=board,
        players=players
    )
    game.start_game()
