from ui.color import ansi
from ui.text import *
from os import system, name


################################################
# Position - Holds position of chess models
################################################
class Position:
    def __init__(self, **kwargs):
        self.row: int = kwargs.get('row', 0)
        self.column: int = kwargs.get('column', 0)

    # * Method - Get step
    def get_step(self, destination: 'Position') -> 'Position':
        row: int = self.row - destination.row
        column: int = self.column - destination.column
        return Position(row=row, column=column)

    # * Methods - Overloaded Operators

    # ! Subtraction
    def __sub__(self, other: 'Position') -> 'Position':
        return Position(
            row=abs(self.row - other.row),
            column=abs(self.column - other.column)
        )

    # ! Addition
    def __add__(self, other: 'Position') -> 'Position':
        return Position(
            row=self.row + other.row,
            column=self.column + other.column
        )

    # ! Equality comparison
    def __eq__(self, other: 'Position') -> bool:
        return self.row == other.row and self.column == other.column

    # * Method - Representation
    def __repr__(self) -> str:
        return f'({self.row}, {self.column})'


#####################################################
# Cell class - Hold cell properties of the board
#####################################################
class Cell:
    def __init__(self, **kwargs):
        self.symbol: str = kwargs.get('symbol', '')
        self.property: Property = kwargs.get('property', Property())
        self.piece_index: int = kwargs.get('piece_index', -1)
        self.type_index: int = kwargs.get('type_index', -1)

    def __repr__(self) -> str:
        return ansi(text=self.symbol, fg=self.property.fg, bg=self.property.bg, style=self.property.style)


# * Function - Hold Screen
def hold(message: Text = Text()) -> None:
    a = input(message)


# * Function - Get allowed input for position on board
def get_position_labels() -> list[str]:
    labels = []

    for row in 'abcdefgh':
        for column in '123456789':
            labels.append(row + column)

    return labels


# * Function - Clear Screen
def clrscr():
    system('cls' if name == 'nt' else 'clear');
