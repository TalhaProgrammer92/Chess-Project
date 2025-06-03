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
        self.__file = open(self.__path, 'r')
        self.__reader = csv.reader(self.__file, delimiter=kwargs.get('delimiter', ','))
    
    # * Getter - CSV Data
    @property
    def data(self) -> list[list[str]]:
        l = list(self.__reader)
        self.close()
        return l
    
    # * Method - Close the opened file
    def close(self) -> None:
        self.__file.close()

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
        self.__file = open(self.__path, self.__mode)
        self.__writer = csv.writer(self.__file, delimiter=kwargs.get('delimiter', ','))
    
    # * Method - Write a single row
    def write_row(self, data: list) -> None:
        self.__writer.writerow(data)
    
    # * Method - Write multiple rows
    def write_rows(self, data: list[list]) -> None:
        self.__writer.writerows(data)

    # * Method - Close the opened file
    def close(self) -> None:
        self.__file.close()

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

    game_csv.close()

    # ? Save pieces data
    piece_csv: Writer = Writer(
        path=path,
        file_name='Pieces',
    	mode='a'
    )

    piece_csv.write_row(game.pieces_handler.header)
    piece_csv.write_rows(game.pieces_handler.data)

    piece_csv.close()

    # ? Save player data
    player_csv: Writer = Writer(
    	path=path,
    	file_name='Player',
    	mode='a'
    )

    player_csv.write_row(game.players[0].header)
    player_csv.write_rows([[game.players[i].data] for i in range(len(game.players))])

    player_csv.close()

# * Function - Load a game
def load_game(slot_name: str) -> tuple | None:
    path: str = f'data/{slot_name}'
    if not exists(path):
        return None
    
    try:
        # ? Player data
        player_data: list = Reader(
            path=path,
            file_name='Player'
        ).data
        next(player_data)

        # ! Convert csv data to player objects' list
        players: list = [
            Player(name=player_data[i][0], score=int(player_data[i][1]), group=player_data[i][2])
            for i in range(len(player_data))
        ]

        # ? Piece data
        piece_data: list[list] = Reader(
            path=path,
            file_name='Pieces'
        ).data
        next(piece_data)

        # ! Convert csv data to piece handler object
        piece_handler: PieceHandler = PieceHandler()
        piece_handler.set_pieces(piece_data)

        # ? Game stats
        game_stats: list = Reader(
            path=path,
            file_name='Game'
        ).data

        # ! Return data / objects
        return game_stats, players, piece_handler

    except Exception:
        print('A file might be missing from the slot!')
        return None
