symbols = '$¢£¥€¤'
codes = []

for symbol in symbols:
    codes.append(ord(symbol)) 

print(codes)

beyond_ascii = [ord(s) for s in symbols if ord(s) > 127]

print(beyond_ascii) 

colors = ['black', 'white']
sizes = ['S', 'M', 'L']
tshirts = [(color, size) for color in colors for size in sizes]

print(tshirts)

for color in colors: 
    for size in sizes:
        print(color, size)
