def f1():
    def lenx():
        lenx = range(3)
        print("In f1's local lenx(), lenx is {}".format(lenx))
        return lenx
    print('In fl(), lenx = {}'.format(lenx)) 
    result = lenx() 
    print('Returning result: {!r}'.format(result)) 
    return result

f1() 

def f2():
    def lenx(): 
        lenx = range(3)
        print("In f2's local lenx(), lenx is {}".format(lenx))
        return lenx

f2() 
