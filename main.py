from ui.color import code
from ui.text import *

from utils.position import *
import utils.settings as settings

from pieces.unicode import *
from pieces.piece import *

if __name__ == '__main__':
    text: Text = Text(
        text='Hello, World!', property=Property(
            fg=code['color']['foreground']['bright']['red'],
            bg=code['color']['background']['dark']['white'],
            style=code['style']['italic'] + code['style']['bold']
        )
    )
    print(text)

    position1, position2 = Position(row=1, column=2), Position(row=4, column=1)
    print(position1 - position2, position1 == position2)

    print(
        chess_piece['white']['king'],
        chess_piece['black']['king'],

        empty_cell['white'],
        empty_cell['black']
    )

    piece1, piece2 = (Piece(symbol=chess_piece['white']['pawn'],
                            color=settings.board_items['color']['white'],
                            position=Position(row=1, column=2)),

                      Piece(symbol=chess_piece['black']['pawn'],
                            color=settings.board_items['color']['black'],
                            position=Position(row=6, column=2)))
    print(piece1, piece2)
    print(piece1.position, piece2.position)
