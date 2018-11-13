import csv

def parse_csv(filename):
    '''
    Parse a CSV file into a list of records 
    '''
    with open(filename) as f:
        rows = csv.reader(f) 

        # read the file headers 
        headers = next(rows)
        records = []
        for row in rows:
            if not row: #skip rows with no data
                continue
            record = dict(zip(headers, row)) 
            records.append(record)
    return records 

portfolio = parse_csv('portfolio.csv')

print(portfolio) 
