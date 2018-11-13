from collections import defaultdict 

pairs = ({'name' : 'Lloyd', 'age' : 36, 'profession' : 'administrator'}) 


d = defaultdict(pairs) 

for key, value in d.item(): 
    print(key, value)


