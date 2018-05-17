import string 

s = 'This quick brown fox jumped over the lazy dog.' 
print(s) 
print(string.capwords(s)) 


# templates 

values = { 'var' : 'foo' } 

t = string.Template(""" 
        Variable            : $var 
        Escape              : $$ 
        Variable in text    : ${var}iable 
        """) 

print('TEMPLATE:', t.substitute(values)) 

s = """ 
        Variable            : %(var)s 
        Escape              : %% 
        Variable in text    : %(var)siable
    """ 
print('INTERPOLATION:', s % values) 

s = """ 
        Variable            : {var} 
        Escape              : {{}} 
        Variable in text: {var}iable
    """ 
print('FORMAT:', s.format(**values)) 
    
