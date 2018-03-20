import csv 

def read_potholes(filename):
    potholes = [] 
    with open(filename) as f:
        rows = csv.reader(f) 
        headers = next(rows) 
        for row in rows:
            record = dict(zip(headers, rows)) 
            potholes.append(record)
    return potholes 

potholes = read_potholes('311-Challenge.csv')

# Find all non-duplicate reports 
nodup = [ row for row in potholes if 'Dup' is not in row['STATUS'] ] 

# Find worst street address 

