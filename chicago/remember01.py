records = []
with open('Data/portfolio.csv', 'rt') as f:
    for line in f:
        row = line.split(',') 
        records.append(row, end="")
