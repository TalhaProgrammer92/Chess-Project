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
                1: 'a',
                2: 'b',
                3: 'c',
                4: 'd',
                5: 'e',
                6: 'f',
                7: 'g',
                8: 'h'
            },

            # ? Columns
            'column': {
                1: '1',
                2: '2',
                3: '3',
                4: '4',
                5: '5',
                6: '6',
                7: '7',
                8: '8'
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

property: dict = {
    'error': Property(
        fg=code['color']['foreground']['bright']['red'],
        style=code['style']['bold'] + code['style']['italic']
    ),

    'warning': Property(
        fg=code['color']['foreground']['dark']['yellow'],
        style=code['style']['italic']
    ),

    'highlight': Property(
        fg=code['color']['foreground']['bright']['green'],
        bg=code['color']['background']['dark']['black'],
        style=code['style']['bold']
    ),

    'player-name': Property(
        fg=code['color']['foreground']['dark']['magenta'],
        style=code['style']['under-line']
    ),

    'piece-position': Property(
        fg=code['color']['foreground']['dark']['magenta'],
        bg=code['color']['background']['bright']['black'],
        style=code['style']['italic']
    )
}

message: dict = {
    'error': {
        'wrong-position': Text(
            text='Incorrect position!',
            property=property['error']
        ),

        'empty-name': Text(
            text='Name cannot be empty!',
            property=property['error']
        ),

        'wrong-entry': Text(
            text='Incorrect number entry!',
            property=property['error']
        ),

        'no-load-game-found': Text(
            text='No game found!',
            property=property['error']
        )
    },

    'warning': {
        'name-already-exist': Text(
            text='Name already exists! Do you want to proceed(Y/N)? ',
            property=property['warning']
        ),

        'king-in-check': Text(
            text='Your king is in check! Do you want to proceed(Y/N)? ',
            property=property['warning']
        )
    },

    'highlight': {
        'player-turn': Text(
            text='The turn of ',
            property=property['highlight']
        )
    }
}
