# Open file 
with open('Data/portfolio.csv', 'rt') as f: 
   headers = next(f) 

   for line in f: 
       row = line.split(',')
       nshares = int(row[1])
       price = float(row[2])
       total_cost += nshares * price 

print('Total cost', total_cost)

# Calculate how much it costs to purchase all shares in the port