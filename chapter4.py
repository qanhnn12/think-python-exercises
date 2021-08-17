# EXERCISE 4.3.1
# Write a function called square that takes a parameter named t, which is a turtle. 
# Write a function call that passes bob as an argument to square, and run the program again.

import turtle

def square(t):
    for i in range(4):
        t.fd(100)
        t.lt(90)

bob = turtle.Turtle()
square(bob)

# EXERCISE 4.3.2
# Add another parameter, named length, to square.

import turtle

def square(t, length):
    for i in range(4):
        t.fd(length)
        t.lt(90)

bob = turtle.Turtle()
square(bob, 250)

# EXERCISE 4.3.3
# Write a n-sided regular polygon by adding a parameter named n.
# Hint: The exterior angles of an n-sided regular polygon are 360/n degrees.

import turtle

def polygon(t, n, length):
    angle = 360 / n
    for i in range(n):
        t.fd(length)
        t.lt(angle)

bob = turtle.Turtle()
polygon(bob, 6, 80)

# EXERCISE 4.3.4
# Write a circle, which takes a radius named r as a parameter.
# Hint: circumference = length * n (n is constant).

import turtle
import math

def polygon(t, n, length):
    angle = 360 / n
    for i in range(n):
        t.fd(length)
        t.lt(angle)

def circle(t, r):
    circumference = 2 * math.pi * r
    n = 60
    length = circumference / n
    polygon(t, n, length)

bob = turtle.Turtle()
circle(bob, 90)

# Rewrite the circle function so n is not constant value.

import turtle
import math

def polygon(t, n, length):
    angle = 360 / n
    for i in range(n):
        t.fd(length)
        t.lt(angle)

def circle(t, r):
    circumference = 2 * math.pi * r
    n = int(circumference / 3) + 3          # Adding 3 to n guarantees that the polygon has at least 3 sides.
    length = circumference / n
    polygon(t, n, length)

bob = turtle.Turtle()
circle(bob, 75)

# EXERCISE 4.3.5
# Write arc function that takes an additional parameter angle, which determines what fraction of a circle to draw.

import turtle
import math

# copy of polygon and transform it into arc    
def arc(t, r, angle):
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = float(angle) / n
    polyline(t, n, step_length, step_angle)
    
# rewrite polygon and arc to use polyline
def polyline(t, n, length, angle):
    for i in range(n):
        t.fd(length)
        t.lt(angle)

def polygon(t, n, length):
    angle = 360.0 / n
    polyline(t, n, length, angle)
  
def circle(t, r):
    arc(t, r, 360)

bob = turtle.Turtle()
arc(bob, 100, 180)
