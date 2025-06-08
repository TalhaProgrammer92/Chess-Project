from board.board import *
from pieces.piece import *
from pieces.handler import *
from player.player import *
from utils.common import *
from logic.misc import *
from ui.text import *
from data.csv_handler import save_game
from data.misc import total_slots
import utils.settings as settings


################################################
# Game - Handle game logic (a single level)
################################################
class Game:
    def __init__(self, **kwargs):
        self.board: Board = kwargs.get('board', None)
        self.players: list[Player] = kwargs.get('players', [Player(), Player()])
        self.moves: int = kwargs.get('moves', 0)
        self.game_over: bool = kwargs.get('game_over', False)
        self.turn: int = kwargs.get('turn', 0)

    # * Getters
    @property
    def header(self) -> list[str]:
        return [
            'game_over',
            'turn',
            'moves'
        ]
    
    @property
    def data(self) -> list:
        return [
            '1' if self.game_over else '0',
            str(self.turn),
            str(self.moves)
        ]

    # * Method - Update game state
    def update(self) -> None:
        self.turn ^= 1  # ? Switch turn

    # * Method - Reset the game
    def reset_game(self) -> None:
        # ! Temperarily avoid TypeError
        if self.board is None:
            return

        self.board.reset()
        self.moves = 0
        self.game_over = False

        for player in self.players:
            player.reset_score()

    # * Method - Take input
    def take_position_input(self, message: Text, _range: list) -> Position | None:
        # ? Take input
        print()
        _input: str = take_input(
            message=message,
            range=_range
        )
        
        # ? Check if user enter 'save' keyword in order to save current game
        if _input == 'save':
            save_game(self, f'slot-{total_slots() + 1}')
            print("Successfully Saved!")
            return self.take_position_input(message, _range)

        # ? Check if user enter 'exit' keyword in order to quit the game
        if _input == 'exit':
            return None
        
        # ? Return
        return parse_labeled_position(_input)

    # * Method - Start the game
    def start_game(self) -> None:
        while not self.game_over:
            # ? Clear Screen
            clrscr()
            
            # ? Display board
            self.board.display()

            # ? Display turn message
            print()
            display_turn(self.players[self.turn])

            # ? Get selected piece location
            position: Position | None = self.take_position_input(
                message=Text(
                    text='Select piece:',
                    property=settings.property['piece-position']
                ),
                
                _range=get_position_labels().extend(['save', 'exit'])
            )

            # ? Quit game
            if position is None:
                return

            # ? Update state
            self.update() 
