import csv
f = open('../Data/portfolio.csv') 
rows = csv.reader(f) 
headers = next(rows) 
row = next(rows)
row
types[1]
types = [str, int, float]
types[1]
types[1](row[1]) 
types[2](row[2]) 
types[1](row[1]) * types[2](row[2]) 
r = list(zip(types, row)) 
r 
converted = [] 
for func, val in zip(types, row): 
    converted.append(func(val)
    ...
    converted.append(func(val))
    ...
    
converted
converted
clear 
converted = [func(val) for func, val in zip(types, row)]
converted
headers
converted
dict(zip(headers, converted)) 
{ name: func(val) for name, func, val in zip(headers, types, row) } 
list(zip(headers, types, row)) 
f = open('../Data/dowstocks.csv') 
rows = csv.reader(f) 
rows
header = next(rows) 
row = next(rows) 
headers 
row
types = [str, float, str, str, float, float, float, float, int] 
converted = [func(val) for func, val in zip(types, row)]
record = dict(zip(headers, converted)
)
record
record['name'] 
quit() 
