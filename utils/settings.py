from ui.color import code

board_items: dict = {
    'color': {
        'cell': {
            'white': code['color']['foreground']['dark']['cyan'],
            'black': code['color']['foreground']['dark']['red']
        },

        'piece': {
            'white': code['color']['foreground']['bright']['cyan'],
            'black': code['color']['foreground']['bright']['red']
        }
    }

}