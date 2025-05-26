from board.board import Board
from pieces.handler import PieceHandler
import utils.settings as settings

if __name__ == '__main__':
    board: Board = Board()
    ph: PieceHandler = PieceHandler()
    ph.reset()

    board.place_pieces(ph.pieces)
    board.display()

    print(
        '',
        settings.message['error']['wrong-position'],
        settings.message['error']['empty-name'],
        settings.message['error']['wrong-entry'],
        sep='\n'
    )
