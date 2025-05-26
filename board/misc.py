from utils.common import *
from utils.settings import *
from ui.text import Property


def get_empty_cell(position: Position) -> Cell:
    index: int = (position.row + position.column) % 2
    symbol: list[str] = [board_items['unicode']['cell']['white'], board_items['unicode']['cell']['black']]
    color: list[str] = [board_items['color']['cell']['white'], board_items['color']['cell']['black']]
    return Cell(symbol=symbol[index], property=Property(fg=color[index]))
