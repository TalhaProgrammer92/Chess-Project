import csv
from os.path import join, exists
from os import mkdir


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
	
	# * Method - Close the opened file
	def close(self) -> None:
		self.__f.close()

	# * Method - Representation
	def __repr__(self) -> str:
		return join(self.__path, self.__file)
	

########################
# Write to csv file
########################
class Writer:
	def __init__(self, **kwargs):
		self.__path: str = kwargs.get('path', '')
		if not exists(self.__path):
			mkdir(self.__path)

		self.__file: str = kwargs.get('file', '') + '.csv'
		self.__mode: str = kwargs.get('mode', 'w')	# ! Can only be either 'w' or 'a'
		self.__f = open(join(self.__path, self.__file), self.__mode)
		self.__writer = csv.writer(self.__f, delimiter=kwargs.get('delimiter', ','))
	
	# * Method - Write a single row
	def write_row(self, data: list) -> None:
		self.__writer.writerow(data)
	
	# * Method - Write multiple rows
	def write_rows(self, data: list[list]) -> None:
		self.__writer.writerows(data)

	# * Method - Close the opened file
	def close(self) -> None:
		self.__f.close()

	# * Method - Representation
	def __repr__(self) -> str:
		return join(self.__path, self.__file) + f' - {self.__mode}'


# * Testing
if '__main__' == __name__:
	# writer: Writer = Writer(path='data', file='file')
	writer: Writer = Writer(path='data', file='file', mode='a')
	# writer.write_rows([
	# 	['name', 'class', 'marks'],
	# 	['Talha Ahmad', 7, 70],
	# 	['Aslam Khan', 7, 62],
	# 	['Ahmad Hassan', 7, 58],
	# 	['Farooq Rajput', 7, 64]
	# ])
	writer.write_rows([
		['Faizan Ali', 7, 72],
		['Akbar', 7],
		['Muzammil', 7, 69]
	])
	writer.close()

	reader: Reader = Reader(path='data', file='file')
	
	# ! Display data
	# print(reader.data)
	for row in reader.data:
		if len(row) > 0:
			# print('|'.join(row))
			print(row)

	reader.close()
