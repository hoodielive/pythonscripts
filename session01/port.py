total = 0.0

with open('example.csv', 'r') as f: 
	for line in f:	
		line = line.strip() #strip whitespace
		parts = line.split(',')
		parts[0] = parts[0].strip('""')
		parts[1] = parts[1].strip('""')
		parts[2] = int(parts[2])
		#parts[3] = float(parts[3])
		#print(parts)
		total += parts[2]
print('Total cost: ', total)
