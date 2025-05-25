from pieces.piece import *


##############################################
# Piece Handler - handle all chess pieces
##############################################
class PieceHandler:
    def __init__(self):
        self.pieces: list = []
        self.__fill()

    # * Method - Fill pieces
    def __fill(self) -> None:
        # ? Lists
        white: list = []
        black: list = []

        # ? Add items - White
        white.extend([Pawn(type='white') for i in range(8)])
        white.extend([
            Rook(type='white'),
            Rook(type='white')
        ])
        white.extend([
            Bishop(type='white'),
            Bishop(type='white')
        ])
        white.extend([
            Knight(type='white'),
            Knight(type='white')
        ])
        white.extend([
            Queen(type='white'),
            King(type='white')
        ])

        # ? Add items - Black
        black.extend([Pawn(type='black') for i in range(8)])
        black.extend([
            Rook(type='black'),
            Rook(type='black')
        ])
        black.extend([
            Bishop(type='black'),
            Bishop(type='black')
        ])
        black.extend([
            Knight(type='black'),
            Knight(type='black')
        ])
        black.extend([
            Queen(type='black'),
            King(type='black')
        ])

        # ? Append to the main list
        self.pieces.append(white)
        self.pieces.append(black)

    # * Method - Reset all positions
    def reset(self) -> None:
        # ? Pawns
        for i in range(8):
            self.pieces[0][i].move(Position(row=6, column=i))
            self.pieces[1][i].move(Position(row=1, column=i))

        # ? Rooks - Bishops - Knights - Queen - King
        index: list = [0, 6]
        for j in range(4):
            for i in range(2):
                piece_index: list = [
                    i + j + (8 if j == 0 else 1),
                    i + j + (8 if j == 0 else 1)
                ]
                self.pieces[0][piece_index[0]].move(Position(row=7, column=index[i]))
                self.pieces[1][piece_index[1]].move(Position(row=0, column=index[i]))
            index[0] += 1
            index[1] -= 1
