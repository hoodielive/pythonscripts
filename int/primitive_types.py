#!/usr/bin/env python3

# a type is a classification of data that spells out possible values for that type and the operations that should be performed on it
# In python 'everything' is an object

# write a program to count the number of bits that are set to 1 in a non-negative integer 
# the program should test bits one at a time starting with the least significant bit. 
# shifting and masking, avoid hard coding the size of the integer word 

def count_bits(x):
    num_bits = 0
    while x:
        num_bits += x & 1 
        x >>= 1
    return num_bits 

count_bits(33)

# since we perform O(1) computation per bit, the time complexity is O(n), where n is the number of bits needed to represent the int, e.g., 4 bits are need to represent 12, which is (1100)^2 in binary. 
