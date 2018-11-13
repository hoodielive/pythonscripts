symbols = 'åß∂ƒ©˙∆˚¬'

# use listcomps and genexps i.e. 'list comprehensions and generator expressions' 

codes = [ord(symbol) for symbol in symbols]

# yields same results but is more sleak and readable 

print(codes) 
