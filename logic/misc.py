from player.player import Player
from utils.common import Position
from ui.text import *
import utils.settings as settings
# import data.csv_handler as csv


# * Function - Display turn
def display_turn(player: Player):
    print(
        settings.message['highlight']['player-turn'],
        Text(text=player.name, property=settings.property['player-name'])
    )


# * Function - Take input
def take_input(message: Text, range: list) -> str:
    while True:
        a = input(message.__repr__() + ' ')
        if a in range:
            return a
        print(settings.message['error']['wrong-entry'])


# * Function - Parse labeled position input
def parse_labeled_position(position: str) -> Position:
    r, c = 'abcdefgh', '123456789'
    position: Position = Position(
        row=r.find(position[0]),
        column=c.find(position[1])
    )
    return position
