from ui.color import code

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
