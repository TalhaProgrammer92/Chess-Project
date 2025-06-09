from ui.color import ansi
from ui.text import Property
from utils.common import *
from board.misc import get_empty_cell
import utils.settings as settings


############################
# Piece - A chess piece
############################
class Piece:
    def __init__(self, **kwargs):
        self._symbol: str = kwargs.get('symbol', '')
        self.property: Property = kwargs.get('property', Property())
        self._position: Position = kwargs.get('position', Position())
        self._valid_moves: list[Position] = []
        self.alive: bool = kwargs.get('alive', True)
        self._group: str = kwargs.get('group', '')

    # * Getters
    @property
    def symbol(self) -> str:
        return self._symbol

    @property
    def position(self) -> Position:
        return self._position
    
    @property
    def group(self) -> str:
        return self._group
    
    @property
    def data(self) -> list:
        return [
            self.position.row,
            self.position.column,
            settings.unicode_map['piece'][self._symbol],
            self._group,
            '1' if self.alive else '0'
        ]

    # * Method - Check displacement
    def displacement(self, destination: Position) -> Position:
        return destination - self._position

    # * Method - Check if steps are clear or enerable/valid
    def are_steps_clear(self, steps: list[Position], board) -> bool:
        # ? Iterate through each step
        # print(steps)
        for step in steps:
            try:
                # ? Get cell at current position i.e. self-position + step
                # print('Piece: {} - Step: {} - Next Step: {}'.format(self.position, step, self.position + step), end=' - ') # ! Debug
                cell: Cell = board.get_cell(self.position + step)

                # ? Check if cell is empty or movable
                cell_group: str = ['white', 'black'][cell.type_index] if cell.type_index != -1 else 'None'
                # print('Cell: {} - Piece Index: {} - Group (Cell): {} - Group (Piece): {}'.format(cell.symbol, cell.piece_index, cell_group, self.group))    # ! Debug
                if cell.piece_index == -1 or cell_group != self.group:
                    return True
                else:
                    break

            except Exception:
                print('Out of Range!')  # ! Debug
                continue
    
        return False

    # * Method - If path is clear
    def is_clear_path(self, destination: Position, board) -> bool:
        # ? Necessary variables
        step: Position = self._position.get_step(destination)
        path: list[Position] = []

        # ? Generate path
        position: Position = self._position
        while position != destination:
            path.append(position)
            # position.row += step.row
            # position.column += step.column
            position += step

        # ? Check the path
        for i in range(len(path)):
            # ? Get the type index
            type_index: int = board.get_cell(path[i]).type_index
            
            # ? If current cell is not empty
            if type_index != -1:
                """
                Case 1: If at last path the cell contain self-group piece then return false
                Case 2: If 'case 1' becomes false then check if it's last cell or not means this cell must be empty
                """
                # ? If the piece belongs to self group
                if ['white', 'black'][type_index] == self.group or i < len(path) - 1:
                    return False

        return True

    # * Method - Check if move is valid
    def is_valid_move(self, destination: Position) -> bool:
        return self.displacement(destination) in self._valid_moves

    # * Method - Move the piece
    def move(self, destination: Position):
        self._position = destination
        return get_empty_cell(self._position)

    # * Method - Representation
    def __repr__(self) -> str:
        return ansi(fg=self.property.fg, bg=self.property.bg, style=self.property.style, text=self._symbol)


###########
# Rook
###########
class Rook(Piece):
    def __init__(self, **kwargs):
        self._group: str = kwargs.get('group', '')
        super().__init__(
            symbol=settings.board_items['unicode']['piece'][self._group]['rook'],
            property=Property(fg=settings.board_items['color']['piece'][self._group]),
            position=kwargs.get('position', Position()),
            group=self._group,
            alive=kwargs.get('alive', True))

        self._valid_moves.extend([Position(row=r, column=0) for r in range(8)])     # Rows
        self._valid_moves.extend([Position(row=0, column=c) for c in range(8)])     # Columns
        self.__score_points: int = 5

    @property
    def score_points(self) -> int:
        return self.__score_points
    
    # * Method - Check if the piece is movable or not
    def is_movable(self, board) -> bool:
        # ? Get all possibile single step positions
        steps: list[Position] = [
            # ! Upward
            Position(row=1, column=0),
            # ! Downward
            Position(row=0, column=1),
            # ! Left
            Position(row=-1, column=0),
            # ! Right
            Position(row=0, column=-1)
        ]
        return self.are_steps_clear(steps, board)


#############
# Knight
#############
class Knight(Piece):
    def __init__(self, **kwargs):
        self._group = kwargs.get('group', '')
        super().__init__(
            symbol=settings.board_items['unicode']['piece'][self._group]['knight'],
            property=Property(fg=settings.board_items['color']['piece'][self._group]),
            position=kwargs.get('position', Position()),
            group=self._group,
            alive=kwargs.get('alive', True))

        self._valid_moves.extend([
            Position(row=2, column=1),
            Position(row=1, column=2)
        ])
        self.__score_points: int = 3

    @property
    def score_points(self) -> int:
        return self.__score_points
    
    # * Method - Check if the piece is movable or not
    def is_movable(self, board) -> bool:
        # ? Get all possibile single step positions
        steps: list[Position] = [
            # ! Top-Right
            Position(row=2, column=1),  # 1
            Position(row=1, column=2),  # 2
            # ! Top-Left
            Position(row=2, column=-1), # 1
            Position(row=1, column=-2), # 2
            # ! Bottom-Left
            Position(row=-2, column=-1),    # 1
            Position(row=-1, column=-2),    # 2
            # ! Bottom-Right
            Position(row=-2, column=1), # 1
            Position(row=-1, column=2)  # 2
        ]
        return self.are_steps_clear(steps, board)


#############
# Bishop
#############
class Bishop(Piece):
    def __init__(self, **kwargs):
        self._group = kwargs.get('group', '')
        super().__init__(
            symbol=settings.board_items['unicode']['piece'][self._group]['bishop'],
            property=Property(fg=settings.board_items['color']['piece'][self._group]),
            position=kwargs.get('position', Position()),
            group=self._group,
            alive=kwargs.get('alive', True))

        self._valid_moves.extend([Position(row=i, column=i) for i in range(8)])
        self.__score_points: int = 3

    @property
    def score_points(self) -> int:
        return self.__score_points
    
    # * Method - Check if the piece is movable or not
    def is_movable(self, board) -> bool:
        # ? Get all possibile single step positions
        steps: list[Position] = [
            # ! Top-Right
            Position(row=1, column=1),
            # ! Top-Left
            Position(row=1, column=-1),
            # ! Bottom-Left
            Position(row=-1, column=-1),
            # ! Bottom-Right
            Position(row=-1, column=1)
        ]
        return self.are_steps_clear(steps, board)


#############
# Queen
#############
class Queen(Piece):
    def __init__(self, **kwargs):
        self._group = kwargs.get('group', '')
        super().__init__(
            symbol=settings.board_items['unicode']['piece'][self._group]['queen'],
            property=Property(fg=settings.board_items['color']['piece'][self._group]),
            position=kwargs.get('position', Position()),
            group=self._group,
            alive=kwargs.get('alive', True))

        self._valid_moves.extend([Position(row=r, column=0) for r in range(8)])     # Rows
        self._valid_moves.extend([Position(row=0, column=c) for c in range(8)])     # Columns
        self._valid_moves.extend([Position(row=i, column=i) for i in range(8)])     # Diagonal
        self.__score_points: int = 9

    @property
    def score_points(self) -> int:
        return self.__score_points
    
    # * Method - Check if the piece is movable or not
    def is_movable(self, board) -> bool:
        # ? Get all possibile single step positions
        steps: list[Position] = [
            # ! Top-Right
            Position(row=1, column=1),
            # ! Top-Left
            Position(row=1, column=-1),
            # ! Bottom-Left
            Position(row=-1, column=-1),
            # ! Bottom-Right
            Position(row=-1, column=1),
            
            # ! Upward
            Position(row=1, column=0),
            # ! Downward
            Position(row=0, column=1),
            # ! Left
            Position(row=-1, column=0),
            # ! Right
            Position(row=0, column=-1)
        ]
        return self.are_steps_clear(steps, board)


###########
# Pawn
###########
class Pawn(Piece):
    def __init__(self, **kwargs):
        self._group: str = kwargs.get('group', '')
        super().__init__(
            symbol=settings.board_items['unicode']['piece'][self._group]['pawn'],
            property=Property(fg=settings.board_items['color']['piece'][self._group]),
            position=kwargs.get('position', Position()),
            group=self._group,
            alive=kwargs.get('alive', True))

        self._valid_moves.extend([
            Position(row=1, column=0),
            Position(row=1, column=1),
            Position(row=2, column=0)   # Special move - Only once in a game
        ])
        self.__double_move_eligible: bool = True
        self.__score_points: int = 1

    @property
    def score_points(self) -> int:
        return self.__score_points

    # * Method (Override)
    def move(self, destination: Position) -> None:
        self._position = destination
        self.__double_move_eligible = False

    # * Method (Override)
    def is_valid_move(self, destination: Position) -> bool:
        displacement: Position = self.displacement(destination)
        if displacement in self._valid_moves:
            return True
        elif not self.__double_move_eligible and Position(row=2, column=0) in self._valid_moves:
            self._valid_moves.remove(Position(row=2, column=0))

        return False

    # * Method - Promote to Queen/Bishop/Rook/Knight
    def promotion(self, piece: str) -> Queen | Bishop | Rook | Knight:
        promote = {
            'queen': lambda: Queen(type=self._group, position=self._position),
            'bishop': lambda: Bishop(type=self._group, position=self._position),
            'rook': lambda: Rook(type=self._group, position=self._position),
            'knight': lambda: Knight(type=self._group, position=self._position)
        }
        return promote[piece]()
    
    # * Method - Check if the piece is movable or not
    def is_movable(self, board) -> bool:
        # ? Get all possibile single step positions
        row_step: int = -1 if self.group == 'white' else 1
        steps: list[Position] = [
            Position(row=row_step, column=0),
            Position(row=row_step, column=1),
            Position(row=row_step, column=-1)
        ]
        return self.are_steps_clear(steps, board)


###########
# King
###########
class King(Piece):
    def __init__(self, **kwargs):
        self._group = kwargs.get('group', '')
        super().__init__(
            symbol=settings.board_items['unicode']['piece'][self._group]['king'],
            property=Property(fg=settings.board_items['color']['piece'][self._group]),
            position=kwargs.get('position', Position()),
            group=self._group,
            alive=kwargs.get('alive', True))

        self._valid_moves.extend([
            Position(row=1, column=1),
            Position(row=0, column=1),
            Position(row=1, column=0)
        ])
        self.__score_points: int = 200

    @property
    def score_points(self) -> int:
        return self.__score_points
    
    # * Method - Check if the piece is movable or not
    def is_movable(self, board) -> bool:
        # ? Get all possibile single step positions
        steps: list[Position] = [
            # ! Top-Right
            Position(row=1, column=1),
            # ! Top-Left
            Position(row=1, column=-1),
            # ! Bottom-Left
            Position(row=-1, column=-1),
            # ! Bottom-Right
            Position(row=-1, column=1),

            # ! Upward
            Position(row=1, column=0),
            # ! Downward
            Position(row=0, column=1),
            # ! Left
            Position(row=-1, column=0),
            # ! Right
            Position(row=0, column=-1)
        ]
        return self.are_steps_clear(steps, board)
