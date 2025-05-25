# from pieces.piece import *
# from board.board import Board
# from utils.position import Position
# from pieces.handler import PieceHandler
from player.player import Player


if __name__ == '__main__':
    # chess_piece: Pawn = Pawn(type='black')
    # print(chess_piece)
    # chess_piece: Knight = chess_piece.promotion('knight')
    # print(chess_piece)
    # chess_piece: Knight = Knight(type='white')
    # print(chess_piece)

    # piece_handle: PieceHandler = PieceHandler()
    # piece_handle.reset()
    #
    # board: Board = Board()
    # board.place_pieces(piece_handle.pieces)
    # board.display()

    player: Player = Player(name='Talha Ahmad')
    player.increment_score(1 * 8 + 2 * (3 + 5) + 9)
    print(player)
