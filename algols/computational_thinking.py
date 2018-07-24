#!/usr/bin/env python3 
# variables 
import turtle 

# vars 
window = turtle.Screen() # create a playground for turtles 
aje = turtle.Turtle() # create a user object 
aje.forward(50)  # -> tell aje to move for 50 units
aje.left(90) # -> tell aje to 'turn' 90 degrees 
aje.forward(30)  # -> tell aje to move for 30 units -> thus completing a rectangle 

# looper
window.mainloop() 
