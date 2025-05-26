from board.board import *
from pieces.piece import *
from pieces.handler import *
from player.player import *
from utils.common import *
import utils.settings as settings


################################################
# Game - Handle game logic (a single level)
################################################
class Game:
    def __init__(self, **kwargs):
        self.board: Board = kwargs.get('board', Board())
        self.players: list[Player] = kwargs.get('players', [Player(), Player()])
        self.pieces_handler: PieceHandler = kwargs.get('pieces', PieceHandler())
        self.moves: int = kwargs.get('moves', 0)
        self.game_over: bool = kwargs.get('game_over', False)

    # * Method - Reset the game
    def reset_game(self) -> None:
        self.board.clear()
        self.pieces_handler.reset()
        self.moves = 0
        self.game_over = False

        for player in self.players:
            player.reset_score()

    # * Method - Start the game
    def start_game(self) -> None:
        pass
