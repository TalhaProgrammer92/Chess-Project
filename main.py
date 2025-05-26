from board.board import Board
from pieces.handler import PieceHandler

if __name__ == '__main__':
    board: Board = Board()
    ph: PieceHandler = PieceHandler()
    ph.reset()

    board.place_pieces(ph.pieces)
    board.display()
