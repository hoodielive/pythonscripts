import csv 
total = 0.0
with open('example.csv') as f:
	rows = csv.reader(f) 
	headers = next(rows) # Skip the header row 
	for row in rows:
		print(type(row[0]))

		row[0] = int(row[0]) # This will generate a ValueError: invalid literal for int() with base 10:
# it is in fact a <str>, so row[0] = row[0].strip() or row[0].replace() - work on later
		row[2] = float(row[2])
		total += row[0] * row[2]
print('Total situation: ', total) 