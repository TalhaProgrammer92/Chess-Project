from ui.color import ansi
from utils.position import *
from board.func import get_empty_cell
import utils.settings as settings


############################
# Piece - A chess piece
############################
class Piece:
    def __init__(self, **kwargs):
        self._symbol: str = kwargs.get('symbol', '')
        self._color: str = kwargs.get('color', '')
        self._position: Position = kwargs.get('position', Position())
        self._valid_moves: list[Position] = []

    # * Getters
    @property
    def symbol(self) -> str:
        return self._symbol

    @property
    def position(self) -> Position:
        return self._position

    # * Method - Check displacement
    def displacement(self, destination: Position) -> Position:
        return destination - self._position

    # * Method - Check if move is valid
    def is_valid_move(self, destination: Position) -> bool:
        return self.displacement(destination) in self._valid_moves

    # * Method - Move the piece
    def move(self, destination: Position):
        self._position = destination
        return get_empty_cell(self._position)

    # * Method - Representation
    def __repr__(self) -> str:
        return ansi(fg=self._color, text=self._symbol)


###########
# Pawn
###########
class Pawn(Piece):
    def __init__(self, _type: str):
        super().__init__(symbol=settings.board_items['unicode']['piece'][_type]['pawn'], color=settings.board_items['color']['piece'][_type])
        self._valid_moves.extend([
            Position(row=1, column=0),
            Position(row=1, column=1),
            Position(row=2, column=0)   # Special move - Only once in a game
        ])
        self.__double_move_eligible: bool = True

    # * Method (Override)
    def move(self, destination: Position) -> tuple[str, str]:
        self._position = destination
        self.__double_move_eligible = False
        return get_empty_cell(self._position)

    # * Method (Override)
    def is_valid_move(self, destination: Position) -> bool:
        displacement: Position = self.displacement(destination)
        if displacement in self._valid_moves:
            return True
        elif not self.__double_move_eligible and Position(row=2, column=0) in self._valid_moves:
            self._valid_moves.remove(Position(row=2, column=0))

        return False


###########
# Rook
###########
class Rook(Piece):
    def __init__(self, _type: str):
        super().__init__(symbol=settings.board_items['unicode']['piece'][_type]['rook'], color=settings.board_items['color']['piece'][_type])
        self._valid_moves.extend([Position(row=r, column=0) for r in range(8)])     # Rows
        self._valid_moves.extend([Position(row=0, column=c) for c in range(8)])     # Columns


#############
# Knight
#############
class Knight(Piece):
    def __init__(self, _type: str):
        super().__init__(symbol=settings.board_items['unicode']['piece'][_type]['knight'], color=settings.board_items['color']['piece'][_type])
        self._valid_moves.extend([
            Position(row=2, column=1),
            Position(row=1, column=2)
        ])


#############
# Bishop
#############
class Bishop(Piece):
    def __init__(self, _type: str):
        super().__init__(symbol=settings.board_items['unicode']['piece'][_type]['bishop'], color=settings.board_items['color']['piece'][_type])
        self._valid_moves.extend([Position(row=i, column=i) for i in range(8)])


#############
# Queen
#############
class Queen(Piece):
    def __init__(self, _type: str):
        super().__init__(symbol=settings.board_items['unicode']['piece'][_type]['queen'], color=settings.board_items['color']['piece'][_type])
        self._valid_moves.extend([Position(row=r, column=0) for r in range(8)])     # Rows
        self._valid_moves.extend([Position(row=0, column=c) for c in range(8)])     # Columns
        self._valid_moves.extend([Position(row=i, column=i) for i in range(8)])     # Diagonal


###########
# King
###########
class King(Piece):
    def __init__(self, _type: str):
        super().__init__(symbol=settings.board_items['unicode']['piece'][_type]['king'], color=settings.board_items['color']['piece'][_type])
        self._valid_moves.extend([
            Position(row=1, column=1),
            Position(row=0, column=1),
            Position(row=1, column=0)
        ])
