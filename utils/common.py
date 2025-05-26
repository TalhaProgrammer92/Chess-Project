from ui.color import ansi
from ui.text import Property


################################################
# Position - Holds position of chess models
################################################
class Position:
    def __init__(self, **kwargs):
        self.__row: int = kwargs.get('row', 0)
        self.__column: int = kwargs.get('column', 0)

    # * Getters
    @property
    def row(self) -> int:
        return self.__row

    @property
    def column(self) -> int:
        return self.__column

    # * Setters
    @row.setter
    def row(self, value: int) -> None:
        if 0 <= value < 8:
            self.__row = value

    @column.setter
    def column(self, value: int) -> None:
        if 0 <= value < 8:
            self.__column = value

    # * Method - Get step
    def get_step(self, destination: 'Position') -> 'Position':
        row: int = self.row - destination.row
        column: int = self.column - destination.column
        return Position(
            row=0 if row == 0 else 1 if row > 0 else -1,
            column=0 if column == 0 else 1 if column > 0 else -1
        )

    # * Methods - Overloaded Operators

    # ! Subtraction
    def __sub__(self, other: 'Position') -> 'Position':
        return Position(row=abs(self.__row - other.row), column=abs(self.__column - other.column))

    # ! Equality comparison
    def __eq__(self, other: 'Position') -> bool:
        return self.__row == other.row and self.__column == other.column

    # * Method - Representation
    def __repr__(self) -> str:
        return f'({self.__row}, {self.__column})'


#####################################################
# Cell class - Hold cell properties of the board
#####################################################
class Cell:
    def __init__(self, **kwargs):
        self.symbol: str = kwargs.get('symbol', '')
        self.property: Property = kwargs.get('property', Property())
        self.piece_index: int = kwargs.get('piece_index', -1)

    def __repr__(self) -> str:
        return ansi(text=self.symbol, fg=self.property.fg, bg=self.property.bg, style=self.property.style)
