from ui.color import code
from ui.text import *
from utils.position import *

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
