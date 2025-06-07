from utils.common import *
from utils.settings import *
from ui.text import Property


def get_empty_cell(position: Position) -> Cell:
    group: str = ['white', 'black'][(position.row + position.column) % 2]
    
    symbol: str = board_items['unicode']['cell'][group]
    
    color: str = board_items['color']['cell'][group]
    
    return Cell(
        symbol=symbol,
        property=Property(fg=color)
    )
