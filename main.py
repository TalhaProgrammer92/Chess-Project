from board.board import Board
from pieces.handler import PieceHandler
from logic.game import *
from player.player import *
from data.csv_handler import *
import utils.settings as settings

if __name__ == '__main__':
    game_stats, players, piece_handler = load_game('slot-1')

    board: Board = Board(piece_handler)

    game: Game = Game(
        board=board, players=players, 
        game_over=True if game_stats[0] == '1' else False,
        turn=int(game_stats[0][1]),
        moves=int(game_stats[0][2])
    )
    game.start_game()
