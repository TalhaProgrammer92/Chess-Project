from board.board import *
from pieces.piece import *
from pieces.handler import *
from player.player import *
from logic.misc import *
from ui.text import *
from data.csv_handler import save_game
from data.misc import total_slots
import utils.settings as settings
import utils.common as common


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
            _range=_range
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

    # * Method - Check if destination is valid
    def is_valid_destination(self, position: Position, destination: Position) -> bool:
        # ? Get piece from given position
        cell: Cell = self.board.get_cell(position)
        type_index, piece_index = cell.type_index, cell.piece_index
        piece = self.board.piece_handler[type_index][piece_index]

        # ? Check if destination is valid
        if not piece.is_valid_move(destination):
            print("Invalid Destination!")   # ! Debug
            return False
        
        # ? Check if path is clear
        is_path_clear: bool = piece.is_clear_path(destination, self.board)
        
        if not is_path_clear: print("Path is not clear!") # ! Debug
        
        return is_path_clear


    # * Method - Check piece selection validation
    def is_valid_piece_selection(self, position: Position) -> bool:
        # ? Get cell at given position
        cell: Cell = self.board.get_cell(position)

        # ? Check if cell is empty or not
        # print('Type index:', cell.type_index) # ! Debug
        if cell.type_index == -1:
            print('Cell is not empty')  # ! Debug & Alert
            return False

        # ? Check if piece belongs to correct group or not
        if cell.type_index != self.turn:
            print('The selected piece does not belong to your group')   # ! Debug & Alert
            return False
        
        # ? Check if piece is movable
        if not self.board.piece_handler.pieces[cell.type_index][cell.piece_index].is_movable(self.board):
            print('Selected piece is not movable!') # ! Debug & Alert
            return False

        return True

    # * Method - Start the game
    def start_game(self) -> None:
        # ? Valid inputs list
        valid_inputs: list = common.get_position_labels()
        valid_inputs.extend(['save', 'load'])
        
        # ? Game-loop
        while not self.game_over:
            # ? Clear Screen
            clrscr()
            
            # ? Display board
            self.board.display()

            # ? Display turn message
            print()
            display_turn(self.players[self.turn])

            # ? Get selected piece location
            while True:
                position: Position | None = self.take_position_input(
                    message=Text(
                        text='Select Position of piece:',
                        property=settings.property['piece-position']
                    ),
                    
                    _range=valid_inputs
                )

                # ? Quit game
                if position is None:
                    return
                
                # ? Check if the piece selection valid
                if self.is_valid_piece_selection(position):
                    break

            # ? Get selected piece destination
            while True:
                destination: Position | None = self.take_position_input(
                    message=Text(
                        text='Select Destination for piece:',
                        property=settings.property['piece-position']
                    ),

                    _range=valid_inputs
                )

                # ? Quit game
                if destination is None:
                    return
                
                # ? Check if the destination is valid
                if self.is_valid_destination(position, destination):
                    break
            
            # ? Move the piece
            self.board.move_piece(position, destination)

            a = input('Movable!')   # ! Hold for debug

            # ? Update state
            self.update()
