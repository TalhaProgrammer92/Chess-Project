from ui.color import ansi, code
# from ui.text import Property
from pieces.handler import PieceHandler
from board.misc import get_empty_cell
from utils.common import *
from utils.settings import board_items


######################################
# Board class - Handle board grid
######################################
class Board:
    def __init__(self, pieces: PieceHandler):
        self.__grid: list[list[Cell]] = []
        self.piece_handler: PieceHandler = pieces
        self.clear()
        self.place_pieces()

    # * Method - Get cell
    def get_cell(self, position: Position) -> Cell:
        return self.__grid[position.row][position.column]

    # * Method - Get Indices
    def get_indices(self, position: Position) -> tuple[int, int]:
        cell: Cell = self.get_cell(position)
        return cell.type_index, cell.piece_index

    # * Method - Move piece
    def move_piece(self, position: Position, destination: Position) -> None:
        # ? Get current cell of given position and indices for piece handler
        current_cell: Cell = self.get_cell(position)
        group_index, piece_index = self.get_indices(position)
        
        # ? Move the piece in handler
        self.piece_handler.pieces[group_index][piece_index].move(destination)
        
        # ? Update the board's grid
        self.set_cell(
            position=destination,
            cell=current_cell
        )
        self.reset_cell(position)

    # * Method - Set cell
    def set_cell(self, **kwargs) -> None:
        position: Position = kwargs.get('position', Position())
        cell: Cell = kwargs.get('cell', Cell())

        self.__grid[position.row][position.column] = cell

    # * Method - Reset cell (Empty)
    def reset_cell(self, position: Position) -> None:
        self.__grid[position.row][position.column] = get_empty_cell(position)

    # * Method - Place pieces from piece handler
    def place_pieces(self) -> None:
        pieces = self.piece_handler.pieces
        for _type in range(len(pieces)):
            for index in range(len(pieces[_type])):
                piece = pieces[_type][index]
                # print('Piece at', piece.position)
                self.set_cell(
                    cell=Cell(
                        symbol=piece.symbol,
                        property=piece.property,
                        piece_index=index,
                        type_index=_type
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
    
    # * Method - Reset board
    def reset(self) -> None:
        self.clear()
        self.piece_handler.reset()
        self.place_pieces()

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
