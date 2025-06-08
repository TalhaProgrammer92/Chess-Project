from os import listdir
from os.path import isdir

total_slots = lambda: len([dir for dir in listdir() if isdir(dir)])
