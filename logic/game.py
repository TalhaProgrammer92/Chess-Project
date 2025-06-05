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
        if self.board is None:  # ! Temperarily avoid TypeError: Board.__init__() missing 1 required positional argument: 'pieces'
            return

        self.board.reset()
        self.moves = 0
        self.game_over = False

        for player in self.players:
            player.reset_score()

    # * Method - Start the game
    def start_game(self) -> None:
        while not self.game_over:
            # ? Clear Screen
            # clrscr()
            # print()
            
            # ? Display board
            self.board.display()

            # ? Display turn message
            print()
            display_turn(self.players[self.turn])

            # ? Get selected piece location
            location: Position = parse_labeled_position(
                take_input(
                    message=Text(
                        text='Select piece: ',
                        property=settings.property['piece-position']
                    ),
                    range=get_position_labels()
                )
            )
            print(location)

            # ? Save Data - Test
            # csv_writer = csv.Writer(path='data/save-01', file='board.csv')
            # data = [['row', 'column', 'symbol']]
            # for row in range(8):
            #     for column in range(8):
            #         data.append([
            #             row, column,
            #             settings.unicode_map['piece'][self.board.get_cell(Position(row=row, column=column)).symbol]
            #         ])

            # csv_writer.write_rows(data)

            # csv_writer.close()
            # print("Successfully saved board data!")

            # ? Hold Screen
            # hold()

            # ? Update state
            self.update()
