from board.board import *
from pieces.piece import *
from pieces.handler import *
from player.player import *
from utils.common import *
from logic.misc import *
from ui.text import *
import utils.settings as settings


################################################
# Game - Handle game logic (a single level)
################################################
class Game:
    def __init__(self, **kwargs):
        self.board: Board = kwargs.get('board', Board())
        self.players: list[Player] = kwargs.get('players', [Player(), Player()])
        self.pieces_handler: PieceHandler = kwargs.get('piece_handler', PieceHandler())
        self.board.place_pieces(self.pieces_handler.pieces)
        self.moves: int = kwargs.get('moves', 0)
        self.game_over: bool = kwargs.get('game_over', False)
        self.turn: int = kwargs.get('turn', 0)

    # * Method - Update game state
    def update(self) -> None:
        self.turn ^= 1  # ? Switch turn

    # * Method - Reset the game
    def reset_game(self) -> None:
        self.board.clear()
        self.pieces_handler.reset()
        self.board.place_pieces(self.pieces_handler.pieces)
        self.moves = 0
        self.game_over = False

        for player in self.players:
            player.reset_score()

    # * Method - Start the game
    def start_game(self) -> None:
        while not self.game_over:
            # ? Display board
            self.board.display()

            # ? Display turn message
            print()
            display_turn(self.players[self.turn])

            # ? Get selected piece location
            location: Position = parse_labeled_position(
                take_input(
                    Text(
                        text='Select piece: ',
                        property=settings.property['piece-position']
                    ),
                    [
                        f'{settings.board_items['unicode']['label']['row'][i + 1]}{settings.board_items['unicode']['label']['column'][i + 1]}'
                        for i in range(8)]
                )
            )
            print(location)

            # ? Hold Screen
            hold()

            # ? Update state
            self.update()
