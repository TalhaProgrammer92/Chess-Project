import csv
from os.path import join, exists
from os import mkdir
from logic.game import Game
from player.player import Player
from pieces.handler import PieceHandler


######################
# Read a csv file
######################
class Reader:
    def __init__(self, **kwargs):
        self.__path: str = join(
            kwargs.get('path', ''),
            kwargs.get('file_name', '') + '.csv'
        )
        self.__delimiter: str = kwargs.get('delimiter', ',')
        self.__data: list[list[str]] | None = None
    
    # * Getter - CSV Data
    @property
    def data(self) -> list[list[str]] | None:
        return self.__data
    
    # * Method - Extract data
    def extract_data(self) -> None:
        with open(self.__path, 'r') as file:
            self.__data = list(csv.reader(file, delimiter=self.__delimiter))
        self.__data = [row for row in self.data if len(row) > 0]    # ! Clean - Filter empty lists

    # * Method - Representation
    def __repr__(self) -> str:
        return self.__path
    

########################
# Write to csv file
########################
class Writer: 
    def __init__(self, **kwargs):
        self.__path: str = kwargs.get('path', '')
        if not exists(self.__path):
            mkdir(self.__path)

        self.__path: str = join(self.__path, kwargs.get('file_name', '') + '.csv')
        self.__mode: str = kwargs.get('mode', 'w')	# ! Can only be either 'w' or 'a'
        self.__delimiter: str = kwargs.get('delimiter', ',')
    
    # * Method - Write a single row
    def write_row(self, data: list) -> None:
        with open(self.__path, self.__mode) as file:
            csv.writer(file, delimiter=self.__delimiter).writerow(data)
    
    # * Method - Write multiple rows
    def write_rows(self, data: list[list]) -> None:
        with open(self.__path, self.__mode) as file:
            csv.writer(file, delimiter=self.__delimiter).writerows(data)

    # * Method - Representation
    def __repr__(self) -> str:
        return join(self.__path, self.__file) + f' - {self.__mode}'


# * Function - Save a game
def save_game(game: Game, slot_name: str) -> None:
    path: str = f'data/{slot_name}'
    
    # ? Save game stats
    game_csv: Writer = Writer(
        path=path,
        file_name='Game'
    )

    game_csv.write_rows([
        game.header,
        game.data
    ])

    # ? Save pieces data
    piece_csv: Writer = Writer(
        path=path,
        file_name='Pieces',
    	mode='a'
    )

    piece_csv.write_row(game.board.piece_handler.header)
    piece_csv.write_rows(game.board.piece_handler.data)

    # ? Save player data
    player_csv: Writer = Writer(
    	path=path,
    	file_name='Player',
    	mode='a'
    )

    player_csv.write_row(game.players[0].header)
    for player in game.players:
        player_csv.write_row(player.data)

# * Function - Load a game
def load_game(slot_name: str) -> tuple[list[str], list[Player], PieceHandler] | None:
    """
    Load a saved game from a specific slot.

    Returns:
        Tuple of (game_stats, players, piece_handler) if successful,
        otherwise None if files are missing or corrupted.
    """
    path: str = f'data/{slot_name}'
    if not exists(path):
        raise FileNotFoundError(f'Particular folder: {slot_name} does not exist')
    
    try:
        # ? Player data
        reader: Reader = Reader(
            path=path,
            file_name='Player'
        )
        reader.extract_data()
        player_data: list = reader.data
        player_data = player_data[1:]
        # print(player_data, end='\n\n')
        # next(player_data)

        # ! Convert csv data to player objects' list
        players: list = [
            Player(name=player_data[i][0], score=int(player_data[i][1]), group=player_data[i][2])
            for i in range(len(player_data))
        ]

        # ? Piece data
        reader = Reader(
            path=path,
            file_name='Pieces'
        )
        reader.extract_data()

        piece_data: list[list] = reader.data
        # print(piece_data, end='\n\n')
        # next(piece_data)

        # ! Convert csv data to piece handler object
        piece_handler: PieceHandler = PieceHandler()
        piece_handler.fill_via_csv_data(piece_data[1:])

        # ? Game stats
        reader = Reader(
            path=path,
            file_name='Game'
        )
        reader.extract_data()
        
        game_stats: list = reader.data
        # print(game_stats, end='\n\n')
        # next(game_stats)

        # ! Return data / objects
        return game_stats[1:], players, piece_handler

    except Exception:
        print('Corrupted Slot!', Exception)
