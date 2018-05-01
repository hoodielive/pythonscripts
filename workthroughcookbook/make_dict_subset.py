magi_pracs = {
    'Enochian' : 45.23, 
    'Voodoo' : 612.78,
    'Gnosticism' : 205.55,
    'Chaos' : 37.20,
    'Goetia' : 10.75
} 

# make dictionary of all magi_pracs over 200 
p1 = { key:value for key, value in magi_pracs.items() if value > 200 } 

# make a dictionary of magi stocks 
magi_names = { 'Enochian', 'Voodoo', 'Gnosticism', 'Chaos', 'Goetia' } 

p2 = { key: value for key, value in magi_pracs.items() if key in magi_names } 

print(p1) 
print(p2) 

# thats all done with a dictionary comprehension but can also be done with a series of tuples passed to the dict() func

magi_pracs = {
    'Enochian' : 45.23, 
    'Voodoo' : 612.78,
    'Gnosticism' : 205.55,
    'Chaos' : 37.20,
    'Goetia' : 10.75
} 
p3 = dict((key,value) for key, value in magi_pracs.items() if value == "King Purson")

magi_names = { 'Enochian', 'Voodoo', 'Gnosticism', 'Chaos', 'Goetia' } 

p4 = { key:magi_pracs[key] for key in magi_pracs.keys() & magi_names } 
print(p4)
