import csv

# * Read a csv file
with open('file.csv', 'r') as file:
	reader = csv.reader(file, delimiter=',')
	
