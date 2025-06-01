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
        self.alive: bool = True
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

    # * Method - If path is clear
    def is_clear_path(self, destination: Position, board_grid: list) -> bool:
        # ? Necessary variables
        step: Position = self._position.get_step(destination)
        path: list[Position] = []

        # ? Generate path
        position: Position = self._position
        while position != destination:
            path.append(position)
            position.row += step.row
            position.column += step.column

        # ? Check the path
        for p in path:
            pass

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
        self._type = kwargs.get('type', '')
        super().__init__(
            symbol=settings.board_items['unicode']['piece'][self._type]['rook'],
            property=Property(fg=settings.board_items['color']['piece'][self._type]),
            position=kwargs.get('position', Position()))

        self._valid_moves.extend([Position(row=r, column=0) for r in range(8)])     # Rows
        self._valid_moves.extend([Position(row=0, column=c) for c in range(8)])     # Columns
        self.__score_points: int = 5

    @property
    def score_points(self) -> int:
        return self.__score_points

    @property
    def type(self) -> str:
        return self._type


#############
# Knight
#############
class Knight(Piece):
    def __init__(self, **kwargs):
        self._type = kwargs.get('type', '')
        super().__init__(
            symbol=settings.board_items['unicode']['piece'][self._type]['knight'],
            property=Property(fg=settings.board_items['color']['piece'][self._type]),
            position=kwargs.get('position', Position()))

        self._valid_moves.extend([
            Position(row=2, column=1),
            Position(row=1, column=2)
        ])
        self.__score_points: int = 3

    @property
    def score_points(self) -> int:
        return self.__score_points

    @property
    def type(self) -> str:
        return self._type


#############
# Bishop
#############
class Bishop(Piece):
    def __init__(self, **kwargs):
        self._type = kwargs.get('type', '')
        super().__init__(
            symbol=settings.board_items['unicode']['piece'][self._type]['bishop'],
            property=Property(fg=settings.board_items['color']['piece'][self._type]),
            position=kwargs.get('position', Position()))

        self._valid_moves.extend([Position(row=i, column=i) for i in range(8)])
        self.__score_points: int = 3

    @property
    def score_points(self) -> int:
        return self.__score_points

    @property
    def type(self) -> str:
        return self._type


#############
# Queen
#############
class Queen(Piece):
    def __init__(self, **kwargs):
        self._type = kwargs.get('type', '')
        super().__init__(
            symbol=settings.board_items['unicode']['piece'][self._type]['queen'],
            property=Property(fg=settings.board_items['color']['piece'][self._type]),
            position=kwargs.get('position', Position()))

        self._valid_moves.extend([Position(row=r, column=0) for r in range(8)])     # Rows
        self._valid_moves.extend([Position(row=0, column=c) for c in range(8)])     # Columns
        self._valid_moves.extend([Position(row=i, column=i) for i in range(8)])     # Diagonal
        self.__score_points: int = 9

    @property
    def score_points(self) -> int:
        return self.__score_points

    @property
    def type(self) -> str:
        return self._type


###########
# Pawn
###########
class Pawn(Piece):
    def __init__(self, **kwargs):
        self._type: str = kwargs.get('type', '')
        super().__init__(
            symbol=settings.board_items['unicode']['piece'][self._type]['pawn'],
            property=Property(fg=settings.board_items['color']['piece'][self._type]),
            position=kwargs.get('position', Position()))

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

    @property
    def type(self) -> str:
        return self._type

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
            'queen': lambda: Queen(type=self._type, position=self._position),
            'bishop': lambda: Bishop(type=self._type, position=self._position),
            'rook': lambda: Rook(type=self._type, position=self._position),
            'knight': lambda: Knight(type=self._type, position=self._position)
        }
        return promote[piece]()


###########
# King
###########
class King(Piece):
    def __init__(self, **kwargs):
        self._type = kwargs.get('type', '')
        super().__init__(
            symbol=settings.board_items['unicode']['piece'][self._type]['king'],
            property=Property(fg=settings.board_items['color']['piece'][self._type]),
            position=kwargs.get('position', Position()))

        self._valid_moves.extend([
            Position(row=1, column=1),
            Position(row=0, column=1),
            Position(row=1, column=0)
        ])
        self.__score_points: int = 200

    @property
    def score_points(self) -> int:
        return self.__score_points

    @property
    def type(self) -> str:
        return self._type
