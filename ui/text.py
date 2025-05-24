from ui.color import ansi


########################################
# Text Property - Colors, and Style
########################################
class Property:
    def __init__(self, **kwargs):
        self.fg: str = kwargs.get('fg', '')
        self.bg: str = kwargs.get('bg', '')
        self.style: str = kwargs.get('style', '')

    # * Method - Add a new style
    def add_style(self, style: str) -> None:
        self.style += style

    # * Method - Clear style
    def clear_style(self) -> None:
        self.style = ''


################################
# Text - Message & Property
################################
class Text:
    def __init__(self, **kwargs):
        self.__text = kwargs.get('text', '')
        self._property = kwargs.get('property', Property())

    # * Getter
    @property
    def text(self) -> str:
        return self.__text

    # * Method - Representation
    def __repr__(self) -> str:
        return ansi(text=self.text, fg=self._property.fg, bg=self._property.bg, style=self._property.style)
