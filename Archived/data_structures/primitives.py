def count_bits(x):
    num_bits = 0
    while x:
        num_bits += x & 1 
        x >>= 1
    print(num_bits)
count_bits(1300) 