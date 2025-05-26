##############################
# Player - Handle players
##############################
class Player:
    def __init__(self, **kwargs):
        self.__name: str = kwargs.get('name', 'unknown')
        self.__score: int = 0

    # * Getters
    @property
    def name(self) -> str:
        return self.__name

    @property
    def score(self) -> int:
        return self.__score

    # * Method - Increase score
    def increment_score(self, score_points: int) -> None:
        self.__score += score_points

    # * Method - Reset Score
    def reset_score(self) -> None:
        self.__score = 0

    # * Method - Representation
    def __repr__(self) -> str:
        return f'Name:\t{self.__name}\nScore:\t{self.score}'
