prices = {
    'Enochian' : 45.23, 
    'Voodoo' : 612.78,
    'Gnosticism' : 205.55,
    'Chaos' : 37.20,
    'Goetia' : 10.75
} 

# make dictionary of all prices over 200 
p1 = { key:value for key, value in prices.items() if value > 200 } 

# make a dictionary of magi stocks 
magi_names = { 'Enochian', 'Voodoo', 'Gnosticism', 'Chaos', 'Goetia' } 

p2 = { key: value for key, value in prices.items() if key in magi_names } 


print(p1) 
print(p2) 
