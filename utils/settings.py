from ui.color import code
from ui.text import *

board_items: dict = {
    # * Colors
    'color': {
        # ? Cell
        'cell': {
            'white': code['color']['foreground']['dark']['cyan'],
            'black': code['color']['foreground']['dark']['red']
        },

        # ? Piece
        'piece': {
            'white': code['color']['foreground']['bright']['cyan'],
            'black': code['color']['foreground']['bright']['red']
        },

        # ? Label
        'label': code['color']['foreground']['bright']['yellow']
    },

    # * Unicodes
    'unicode': {
        # ? Cell
        'cell': {
            'white': '○',
            'black': '◉'
        },

        # ? Piece
        'piece': {
            # ? White
            'white': {
                'king': '♔',
                'queen': '♕',
                'rook': '♖',
                'bishop': '♗',
                'knight': '♘',
                'pawn': '♙'
            },

            # ? Black
            'black': {
                'king': '♚',
                'queen': '♛',
                'rook': '♜',
                'bishop': '♝',
                'knight': '♞',
                'pawn': '♟'
            }
        },

        # ? Labels
        'label': {
            # ? Rows
            'row': {
                1: 'ⓐ',
                2: 'ⓑ',
                3: 'ⓒ',
                4: 'ⓓ',
                5: 'ⓔ',
                6: 'ⓕ',
                7: 'ⓖ',
                8: 'ⓗ'
            },

            # ? Columns
            'column': {
                1: '①',
                2: '②',
                3: '③',
                4: '④',
                5: '⑤',
                6: '⑥',
                7: '⑦',
                8: '⑧'
            }
        }
    }
}

player: dict = {
    'color': {
        'name': code['color']['foreground']['bright']['green'],
        'score': code['color']['foreground']['bright']['magenta']
    }
}

__property: dict = {
    'error': Property(
        fg=code['color']['foreground']['bright']['red'],
        style=code['style']['bold'] + code['style']['italic']
    ),

    'warning': Property(
        fg=code['color']['foreground']['dark']['yellow'],
        style=code['style']['italic']
    )
}

message: dict = {
    'error': {
        'wrong-position': Text(
            text='Incorrect position!',
            property=__property['error']
        ),

        'empty-name': Text(
            text='Name cannot be empty!',
            property=__property['error']
        ),

        'wrong-entry': Text(
            text='Incorrect number entry!',
            property=__property['error']
        ),

        'no-load-game-found': Text(
            text='No game found!',
            property=__property['error']
        )
    },

    'warning': {
        'name-already-exist': Text(
            text='Name already exists! Do you want to proceed(Y/N)? ',
            property=__property['warning']
        ),

        'king-in-check': Text(
            text='Your king is in check! Do you want to proceed(Y/N)? ',
            property=__property['warning']
        )
    }
}
