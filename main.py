from pieces.piece import *
from board.board import Board
from utils.position import Position

if __name__ == '__main__':
    # chess_piece: Pawn = Pawn(type='black')
    # print(chess_piece)
    # chess_piece: Knight = chess_piece.promotion('knight')
    # print(chess_piece)
    # chess_piece: Knight = Knight(type='white')
    # print(chess_piece)

    board: Board = Board()
    board.place_pieces([
        Pawn(type='white', position=Position(row=1, column=2)),
        Pawn(type='white', position=Position(row=1, column=3))
    ])
    board.display()
