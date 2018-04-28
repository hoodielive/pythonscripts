total = 0.0 
with open('portfolio2.csv', 'r') as f:
    headers = next(f) 
    for line in f:
        line = line.strip() # get rid of white space 
        parts = line.split(',') # convert to a list so that you can massage data ( clean up data ) 
        
        # massage data 
        parts[0] = parts[0].strip('"') 
        parts[1] = parts[1].strip('"') 
        parts[2] = int(parts[2])
        parts[3] = float(parts[3])
        total += parts[2]*parts[3]
        print("The Total is:", total)  
