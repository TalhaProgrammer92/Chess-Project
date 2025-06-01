from pieces.piece import *


##############################################
# Piece Handler - handle all chess pieces
##############################################
class PieceHandler:
    def __init__(self):
        self.pieces: list = []
        self.__fill()
    
    # * Getters
    @property
    def header(self) -> list[str]:
        return [
            'row',
            'column',
            'type',
            'group',
            'alive'
        ]

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
            self.pieces[0][i].move(Position(row=6, column=i))  # White
            self.pieces[1][i].move(Position(row=1, column=i))  # Black

        # ? Rooks
        self.pieces[0][8].move(Position(row=7, column=0))
        self.pieces[0][9].move(Position(row=7, column=7))
        self.pieces[1][8].move(Position(row=0, column=0))
        self.pieces[1][9].move(Position(row=0, column=7))

        # ? Bishops
        self.pieces[0][10].move(Position(row=7, column=1))
        self.pieces[0][11].move(Position(row=7, column=6))
        self.pieces[1][10].move(Position(row=0, column=1))
        self.pieces[1][11].move(Position(row=0, column=6))

        # ? Knights
        self.pieces[0][12].move(Position(row=7, column=2))
        self.pieces[0][13].move(Position(row=7, column=5))
        self.pieces[1][12].move(Position(row=0, column=2))
        self.pieces[1][13].move(Position(row=0, column=5))

        # ? Queens
        self.pieces[0][14].move(Position(row=7, column=3))
        self.pieces[1][14].move(Position(row=0, column=3))

        # ? Kings
        self.pieces[0][15].move(Position(row=7, column=4))
        self.pieces[1][15].move(Position(row=0, column=4))

