from utils.position import *
from utils.settings import *


def get_empty_cell(position: Position) -> tuple[str, str]:
    index: int = (position.row + position.column) % 2
    symbol: list[str] = [board_items['unicode']['cell']['white'], board_items['unicode']['cell']['black']]
    color: list[str] = [board_items['color']['cell']['white'], board_items['color']['cell']['black']]
    return symbol[index], color[index]
