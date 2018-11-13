#!/usr/bin/env python3 

ages = [ 3, 5, 7, 12, 15, 17, 18, 20, 22, 23, 27 ] 

for age in ages:
    isAdult = age > 17
    if not isAdult:
        print("Being " + str(age) + " does not make you an adult.") 
    else:
        print("You have been granted access because you are", age) 


