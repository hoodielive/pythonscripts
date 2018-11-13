from collections import deque 

def search(lines, pattern, history=5):
    previous_lines = deque(maxlen=history) 
    for line in lines:
        if pattern in line:
            yield line, previous_lines
        previous_lines.append(line) 

# Example use on a file
if __name__ == '__main__':
    with open('portfolio.csv') as f:
        for line, prevlines in search(f, 'python', 5):
            for pline in prevlines:
                print(pline, end='') 
            print(line, end='') 
            print('-'*20) 

# Return stuff 
q = deque(maxlen=3) 
q.append((1,2,3)) 
q.appendleft((4,5,6))
print(q) 

list = [7, 8, 9]
a = deque(maxlen=3)
a.extend(q)

print(type(q))  
print(type(a))  
print(a) 
