
# * Store unicode of chess pieces
chess_piece: dict = {
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

# * Store unicode of empty cells
empty_cell: dict = {
    'white': '○',
    'black': '◉'
}
