from collections import defaultdict

pairs = ({ 'name' : 'lawrence', 'age' : 23 }) 

#    for key, value in pairs:
#        if key not in d:
#            d[key] = [] 
#        d[key].append(value) 


d = defaultdict(list) 
for key, value in pairs.items(): 
    d[key].append(value) 
print(d)
