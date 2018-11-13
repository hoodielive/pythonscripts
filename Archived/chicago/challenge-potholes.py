import re
with open('/home/lucid/Downloads/311_Service_Requests_-_Pot_Holes_Reported.csv', 'rt') as f:
    headers = next(f)
    for line in f:
        row = line.split(',')
        