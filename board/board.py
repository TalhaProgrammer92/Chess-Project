from ui.color import ansi
from ui.text import Property
from board.misc import get_empty_cell
from utils.position import Position


#####################################################
# Cell class - Hold cell properties of the board
#####################################################
class Cell:
    def __init__(self, **kwargs):
        self.symbol: str = kwargs.get('symbol', '')
        self.property: Property = kwargs.get('property', Property())

    def __repr__(self) -> str:
        return ansi(text=self.symbol, fg=self.property.fg, bg=self.property.bg, style=self.property.style)


######################################
# Board class - Handle board grid
######################################
class Board:
    def __init__(self):
        self.grid: list[list[Cell]] = []

    # * Method - Clear game board
    def clear(self) -> None:
        # ? If grid is empty
        if len(self.grid) == 0:
            for row in range(8):
                l: list[Cell] = []
                for column in range(8):
                    symbol, color = get_empty_cell(Position(row=row, column=column))
                    l.append(Cell(symbol=symbol, property=Property(fg=color)))
                self.grid.append(l)
        # ? If grid is already filled
        else:
            for row in range(8):
                for column in range(8):
                    symbol, color = get_empty_cell(Position(row=row, column=column))
                    self.grid[row][column] = Cell(symbol=symbol, property=Property(fg=color))
