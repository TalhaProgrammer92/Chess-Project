import csv
from os.path import join


######################
# Read a csv file
######################
class Reader:
	def __init__(self, **kwargs):
		self.__path: str = kwargs.get('path', '')
		self.__file: str = kwargs.get('file', '') + '.csv'
		self.__f = open(join(self.__path, self.__file), 'r')
		self.__reader = csv.reader(self.__f, delimiter=kwargs.get('delimiter', ','))
	
	# * Getter - CSV Data
	@property
	def data(self) -> list[list[str]]:
		return list(self.__reader)

	# * Method - Representation
	def __repr__(self) -> str:
		return join(self.__path, self.__file)
	

########################
# Write to csv file
########################
class Writer:
	def __init__(self, **kwargs):
		self.__path: str = kwargs.get('path', '')
		self.__file: str = kwargs.get('file', '') + '.csv'
		self.__f = open(join(self.__path, self.__file), 'r')
		self.__writer = csv.writer(self.__f, delimiter=kwargs.get('delimiter', ','))
	
	# * Method - Representation
	def __repr__(self) -> str:
		return join(self.__path, self.__file)


# * Testing
if '__main__' == __name__:
	reader: Reader = Reader(path='data', file='file')
	
	# ! Display data
	# print(reader.data)
	for row in reader.data:
		print('|'.join(row))
