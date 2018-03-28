# lists, sets, strings, tuples, dictionaries, deque, heaps 


# dictionaires
dict = {
        'name' : 'esu', 
        'age' : 32394390438,
        'city' : 'Nigeria' 
} 

print(dict['name']) 

for key, value in dict.items(): 
    print(key, value)


# lists, they are indexed  
list = [1,2,3,4] 
print(list) 
print(list[2]) 
print(list[-1]) 

for item in list:
    item += 1
    print(item) 



# Functional Programs only in Python 3.4 and above
# map(function, list), filter(function, list), reduce(function,list) lambda, list comprehension 

# map much like a for loop that can be used to apply an operation on each item and then return a result 

list = [1,2,3,4] 
items = [1,2,3,4,5] 
def inc(x): return x + 1 
inc(42) 



