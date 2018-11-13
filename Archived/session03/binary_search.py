my_list = [1,3,5,7,9]
low = 0
high = len(my_list) - 1
mid = (low + high) / 2 
guess = 15
item = 20030

if guess < item: 
    low = mid + 1 

def binary_search(my_list, item): 
    low = 0 
    high = len(my_list) - 1
    
    while low <= high: 
        mid = (low + high) 
        guess = my_list[mid]
        if guess == item: 
            high = mid - 1
        if guess > item: 
            high  = mid - 1
        else: 
            low = mid + 1
    return None 

print(binary_search(my_list, 3))
