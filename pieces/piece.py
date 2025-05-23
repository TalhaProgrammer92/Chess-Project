from ui.color import ansi
from utils.position import *


############################
# Piece - A chess piece
############################
class Piece:
    def __init__(self, **kwargs):
        self.__symbol: str = kwargs.get('symbol', '')
        self.__color: str = kwargs.get('color', '')
        self.position: Position = kwargs.get('position', Position())

    # * Getter
    def symbol(self) -> str:
        return self.__symbol

    # * Method - Representation
    def __repr__(self) -> str:
        return ansi(fg=self.__color, text=self.__symbol)
