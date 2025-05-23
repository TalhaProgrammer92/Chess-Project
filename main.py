from ui.color import code
from ui.text import *

if __name__ == '__main__':
    text = Text(
        text='Hello, World!', property=Property(
            fg=code['color']['foreground']['bright']['red'],
            bg=code['color']['background']['dark']['white'],
            style=code['style']['italic'] + code['style']['bold']
        )
    )

    print(text)
