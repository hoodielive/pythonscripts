import csv 

def read_portfolio(filename):
    portfolio = []
    with open(filename, 'rt') as f: 
        rows = csv.reader(f) 
        headers = next(rows)
        for row in rows:
            parse_seq = {
                'name': row[0], 
                'shares': int(row[1]), 
                'price': float(row[2])
            }
            portfolio.append(parse_seq)
    return portfolio 

# Dictionary 
portfolio = read_portfolio('../Data/portfolio.csv')
print(portfolio[1])
total = 0.0 
for s in portfolio:
    total += s['shares'] * s['price']

print(total)
# Dictionary

def read_prices(filename): 
    prices = { }
    prices['IBM'] = 92.45
    prices['MSFT'] = 45.12
    print(prices)
    with open(filename) as f: 
        rows = csv.reader(f)
        for row in rows: 
            try:
                prices[row[0]] = float(row[1])
            except IndexError:
                pass
    return prices 
read_prices('../Data/prices.csv')

def print_report(reportdata):
	headers = ('Name', 'Shares', 'Price', 'Change')
	print('%10s %10s %10s %10s' % headers)
        print(('-'*10 + ' ')*len(headers))
        	for row in reportdata:
        	print('%10s %10d %10.2f %10.2f' % row)

def portfolio_report(portfolio_filename, prices_filename):
	portfolio = read_portfolio(portfoliofile)
	prices = read_prices(pricefile)
	report = make_report_data(portfolio, prices) 
	print_report(report)

portfolio_report('../Data/portfolio.csv', '../Data/prices.csv') 	
