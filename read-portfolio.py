def read_portfolio(filename, *, errors='warn'):
	''' 
	Read a CSV file with name, date, shares, price data into a list
	'''
	if errors not in { 'warn', 'silent', 'raise' }: 
		raise ValueError("errors must be of 'warn', 'silent', 'raise'")

	portfolio = [] 
	total = 0.0 
	with open(filename, 'r') as f:
		rows = csv.reader(f) 
		headers = next(rows) # Skip the header row for now
		for rowno, row in enumerate(rows, start=1):
			try:
				row[2] = int(row[2])
				row[3] = float(row[3])
			except ValueError as err:
				if errors == 'warn': 
					print('Row:', rowno, 'Bad row:', row)
					print('Row:', rowno, 'Reason:', err)
				elif errors == 'raise':
					raise # Reraises the last exception 
				else:
					pass 
				continue
			record = tuple(row)# . . .(row[0], row[1], row[2], row[3])  
			portfolio.append(record)
	return portfolio 

	portfolio = read_portfolio('example.csv')
	print(portfolio)
	total = read_portfolio('example.csv', errors='silent')
	print('Total cost: ', total)