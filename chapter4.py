## Exercise 4.3.1.
# Write a function called square that takes a parameter named t, which is a turtle. 
# Write a function call that passes bob as an argument to square, and run the program again.

import turtle

def square(t):
    for i in range(4):
        t.fd(100)
        t.lt(90)

bob = turtle.Turtle()
square(bob)

## Exercise 4.3.2.
# Add another parameter, named length, to square.

import turtle

def square(t, length):
    for i in range(4):
        t.fd(length)
        t.lt(90)

bob = turtle.Turtle()
square(bob, 250)

## Exercise 4.3.3.
# Draw a n-sided regular polygon polygon by adding a parameter named n..
# Hint: The exterior angles of an n-sided regular polygon are 360/n degrees.

import turtle

def polygon(t, n, length):
    angle = 360 / n
    for i in range(n):
        t.fd(length)
        t.lt(angle)

bob = turtle.Turtle()
polygon(bob, 6, 80)

## Exercise 4.3.4.
# Draw circle, which takes a radius, r, as a parameter.
# Hint: circumference = length * n

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


