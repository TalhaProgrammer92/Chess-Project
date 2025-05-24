from pieces.piece import *

if __name__ == '__main__':
    chess_piece: Pawn = Pawn(type='black')
    print(chess_piece)
    chess_piece: Knight = chess_piece.promotion('knight')
    print(chess_piece)
    chess_piece: Knight = Knight(type='white')
    print(chess_piece)
