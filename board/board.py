from ui.color import ansi, code
from ui.text import Property
from board.misc import get_empty_cell
from utils.common import *
from utils.settings import board_items


######################################
# Board class - Handle board grid
######################################
class Board:
    def __init__(self):
        self.__grid: list[list[Cell]] = []
        self.clear()

    # * Method - Get cell
    def get_cell(self, position: Position) -> Cell:
        return self.__grid[position.row][position.column]

    # * Method - Set cell
    def set_cell(self, **kwargs) -> None:
        position: Position = kwargs.get('position', Position())
        cell: Cell = kwargs.get('cell', Cell())

        self.__grid[position.row][position.column] = cell

    # * Method - Reset cell (Empty)
    def reset_cell(self, position: Position) -> None:
        self.__grid[position.row][position.column] = get_empty_cell(position)

    # * Method - Place pieces
    def place_pieces(self, pieces: list) -> None:
        for t in range(len(pieces)):
            for index in range(len(pieces[t])):
                piece = pieces[t][index]
                self.set_cell(
                    cell=Cell(
                        symbol=piece.symbol,
                        property=piece.property,
                        piece_index=index,
                        type_index=t
                    ),
                    position=piece.position,
                )

    # * Method - Clear game board
    def clear(self) -> None:
        # ? If grid is empty
        if len(self.__grid) == 0:
            for row in range(8):
                l: list[Cell] = []
                for column in range(8):
                    l.append(get_empty_cell(Position(row=row, column=column)))
                self.__grid.append(l)

        # ? If grid is already filled
        else:
            for row in range(8):
                for column in range(8):
                    self.__grid[row][column] = get_empty_cell(Position(row=row, column=column))

    # * Method - Display the grid
    def display(self) -> None:
        color: str = board_items['color']['label']

        # ? Column - numbers
        print(' ' * 2, end='')
        for i in range(8):
            num: str = ansi(text=board_items['unicode']['label']['column'][i + 1], fg=color)
            print(num, end=' ' if i < 7 else '')
        print()

        # ? Cells
        for row in range(8):
            print(ansi(text=board_items['unicode']['label']['row'][row + 1], fg=color), end=' ')    # ? Row - numbers
            for column in range(8):
                print(self.__grid[row][column], end=' ')
            print()
