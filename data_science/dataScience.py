import numpy as np 
from math import pi 

x = 5
print(x) 
print(x + 2) 
print(x*2)
print(x**2) 
print(x%2) 
print(x/float(2)) 
print(str(x)) 

# Numpy Arrays 
my_list = [1,2,3,4]
my_array = np.array(my_list) 
print(my_array[1])
print(my_array.shape) 
np.insert(my_array, 1, 5)
