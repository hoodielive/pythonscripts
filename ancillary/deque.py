from collections import deque 

def search(lines, patterns, history=5):
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


q = deque(maxlen=3) 
q.append((1,2,3)) 

