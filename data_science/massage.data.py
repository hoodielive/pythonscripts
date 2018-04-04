import os,sys

with open('Data/portfolio.csv', 'rt') as f:
    headers = next(f) 
    for line in f:
        row = line.split(',') 
        print(headers)
        print(line, end="") 


