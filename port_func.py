import csv
def exa(filename):
	'''
	Computes total for a csv file with name, data, share, price data 
	'''
	total = 0.0

	with open(filename, 'rt') as f:
		rows = csv.reader(f)
		headers = next(rows) # Skip header row
		for row in rows:
			row[2] = int(row[2])
			row[3] = float(row[3])
			total += row[2] * row[3]
	return total 

total = exa('Data/<file>')
print('Total cost: ', total)