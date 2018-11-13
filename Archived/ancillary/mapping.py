#    research = {
#        'name' : 'Lawrence', 
#        'book' : 'Elevate!', 
#        'science' : 'mysticism'
#    } 

research = {
        'name' : 'Lawrence', 
} 

d = {} 

for key, value in research: 
    if key not in d:
        d[key] = [] 
    d[key].append(value) 


