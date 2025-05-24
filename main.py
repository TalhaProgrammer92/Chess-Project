from pieces.piece import *

if __name__ == '__main__':
    chess_piece: Pawn = Pawn(_type='white')
    destination: Position = Position(row=2, column=0)
    print(chess_piece.is_valid_move(destination))
    chess_piece.move(destination)
    print(chess_piece.is_valid_move(destination))
    print(chess_piece.is_valid_move(destination))

    chess_piece: Queen = chess_piece.promotion('queen')
    destination = Position(row=1, column=0)
    print(chess_piece.is_valid_move(destination))
