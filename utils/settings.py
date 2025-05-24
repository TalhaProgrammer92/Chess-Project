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
        }
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
        }
    }

}