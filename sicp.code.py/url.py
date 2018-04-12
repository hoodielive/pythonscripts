from urllib.request import urlopen

shakesphere = urlopen('http://inst.eecs.berkeley.edu/~cs61a/fa11/shakespeare.txt')

words = set(shakesphere.read().decode().split()) 

compute_algol = { w for w in words if len(w) >= 5 and w[::-1] in words } 

for w in words:
    if len(w) >= 5:
        print(w[::-1]) 

#print(words) 
#print(compute_algol) 
