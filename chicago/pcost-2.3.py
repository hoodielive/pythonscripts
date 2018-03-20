import sys,os,csv

def portfolio_cost(filename): 
    with open(filename, 'rt') as f: 
        rows = csv.reader(f)
        headers = next(rows) 
        for rowno, row in enumerate(rows, start=1): 
            record = dict(zip(headers, row)) 
            try: 
                nshares = int(record['shares']) 
                price = float(record['price']) 
                total_cost += nshares * price
            except ValueError:
                print(f'Row {rowno}: Bad row: {row}') 

portfolio_cost()
