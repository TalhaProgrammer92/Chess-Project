from pieces.piece import *


##############################################
# Piece Handler - handle all chess pieces
##############################################
class PieceHandler:
    def __init__(self):
        self.pieces: list[list[Pawn | Bishop | Rook | Knight | Queen | King]] = [[], []]
        # self.fill_default()
    
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
    
    @property
    def data(self) -> list[list]:
        d: list[list] = []
        for pieces in self.pieces:
            for piece in pieces:
                d.append(piece.data)
        return d

    # * Method - Fill pieces
    def fill_default(self) -> None:
        # ? Lists
        white: list = []
        black: list = []

        # ? Add items - White
        white.extend([Pawn(group='white') for i in range(8)])
        white.extend([
            Rook(group='white'),
            Rook(group='white')
        ])
        white.extend([
            Bishop(group='white'),
            Bishop(group='white')
        ])
        white.extend([
            Knight(group='white'),
            Knight(group='white')
        ])
        white.extend([
            Queen(group='white'),
            King(group='white')
        ])

        # ? Add items - Black
        black.extend([Pawn(group='black') for i in range(8)])
        black.extend([
            Rook(group='black'),
            Rook(group='black')
        ])
        black.extend([
            Bishop(group='black'),
            Bishop(group='black')
        ])
        black.extend([
            Knight(group='black'),
            Knight(group='black')
        ])
        black.extend([
            Queen(group='black'),
            King(group='black')
        ])

        # ? Append to the main list
        self.pieces[0] = white
        self.pieces[1] = black

    # * Method - Set positions from given pieces' data
    def fill_via_csv_data(self, pieces_data: list[list]):
        # ? Iterate through each piece's data
        for piece in pieces_data:
            # ! Extracted Data from CSV
            group: str = piece[3]
            group_index: int = 0 if group == 'white' else 1
            position: Position = Position(
                row=int(piece[0]),
                column=int(piece[1])
            )
            alive: bool = True if piece[4] == '1' else False

            # ? Set piece
            match piece[2].lower():
                # ! Pawn
                case 'p':
                    self.pieces[group_index].append(
                        Pawn(
                            group=group,
                            position=position,
                            alive=alive
                        )
                    )
                
                # ! Rook
                case 'r':
                    self.pieces[group_index].append(
                        Rook(
                            group=group,
                            position=position,
                            alive=alive
                        )
                    )
                
                # ! Knight
                case 'n':
                    self.pieces[group_index].append(
                        Knight(
                            group=group,
                            position=position,
                            alive=alive
                        )
                    )
                
                # ! Bishop
                case 'b':
                    self.pieces[group_index].append(
                        Bishop(
                            group=group,
                            position=position,
                            alive=alive
                        )
                    )
                
                # ! Queen
                case 'q':
                    self.pieces[group_index].append(
                        Queen(
                            group=group,
                            position=position,
                            alive=alive
                        )
                    )
                
                # ! King
                case 'k':
                    self.pieces[group_index].append(
                        King(
                            group=group,
                            position=position,
                            alive=alive
                        )
                    )

    # * Method - Reset all positions
    def reset(self) -> None:
        self.fill_default()

        # ? Pawns
        for i in range(8):
            self.pieces[0][i].move(Position(row=6, column=i))  # ! White
            self.pieces[1][i].move(Position(row=1, column=i))  # ! Black

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

