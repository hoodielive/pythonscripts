class Person:
    def __init__(self, name, address):
        self.name = name
        self.address = address

age = Person()  
age.name = "larry"
age.address = "2014 Somewhere over the rainbox"
print(age.name, age.address)
