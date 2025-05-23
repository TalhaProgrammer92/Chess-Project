from UI.color import *

if __name__ == '__main__':
    print(
        ansi(
            'Hello,',
            code['color']['foreground']['bright']['yellow'],
            code['color']['background']['dark']['white'],
            code['style']['bold']
        ),
        ansi(
            'World!',
            code['color']['foreground']['dark']['red'],
            code['color']['background']['bright']['cyan'],
            code['style']['italic'] + code['style']['under-line']
        )
    )
