from pieces.piece import *

if __name__ == '__main__':
    pawn: Pawn = Pawn(_type='white')
    destination: Position = Position(row=2, column=0)
    print(pawn.is_valid_move(destination))
    pawn.move(destination)
    print(pawn.is_valid_move(destination))
    print(pawn.is_valid_move(destination))
