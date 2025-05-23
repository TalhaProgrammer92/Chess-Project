# * ANSI Codes
code: dict = {
    'color': {
        # ? Foreground colors
        'foreground': {
            'bright': {
                'black': '\033[90m',
                'red': '\033[91m',
                'green': '\033[92m',
                'yellow': '\033[93m',
                'blue': '\033[94m',
                'magenta': '\033[95m',
                'cyan': '\033[96m',
                'white': '\033[97m'
            },

            'dark': {
                'black': '\033[30m',
                'red': '\033[31m',
                'green': '\033[32m',
                'yellow': '\033[33m',
                'blue': '\033[34m',
                'magenta': '\033[35m',
                'cyan': '\033[36m',
                'white': '\033[37m'
            }
        },

        # ? Background Colors
        'background': {
            'bright': {
                'black': '\033[100m',
                'red': '\033[101m',
                'green': '\033[102m',
                'yellow': '\033[103m',
                'blue': '\033[104m',
                'magenta': '\033[105m',
                'cyan': '\033[106m',
                'white': '\033[107m'
            },

            'dark': {
                'black': '\033[40m',
                'red': '\033[41m',
                'green': '\033[42m',
                'yellow': '\033[43m',
                'blue': '\033[44m',
                'magenta': '\033[45m',
                'cyan': '\033[46m',
                'white': '\033[47m'
            }
        }
    },

    # ? Styles
    'style': {
        'bold': '\033[1m',
        'dim': '\033[2m',
        'italic': '\033[3m',
        'under-line': '\033[4m',
        'blink': '\033[5m',
        'reverse': '\033[6m',
        'hidden': '\033[7m'
    },

    # ? Reset
    'reset': '\033[0m'
}


# * Function to get ansi encoded string
def ansi(**kwargs) -> str:
    fg: str = kwargs.get('fg', '')
    bg: str = kwargs.get('bg', '')
    style: str = kwargs.get('style', '')
    text: str = kwargs.get('text', '')
    return fg + bg + style + text + code['reset']
