# EXERCISE 5.1: Converts it to a time of day in hours, minutes, and seconds, plus the number of days since the epoch.

import time
total_secs = time.time()

# seconds = the remainder of total seconds divided by the number of seconds in a minute 
# minutes = the remainder of total minutes divided by the number of minutes in an hour
# the same applies for hours and days

seconds = int(total_secs % 60)
minutes = int((total_secs // 60) % 60)
hours = int((total_secs // 3600) % 24)
days = int(total_secs // (3600 * 24))

print("There have been", str(days), "days,", str(hours), " hours,", str(minutes), "minutes, and", str(seconds), "seconds since epoch.")


# EXERCISE 5.2: Check the Fermat’s Last Theorem

def check_format(a, b, c, n):
    if n > 2 and a**n + b**n == c**n:
        print("Holy smokes, Fermat was wrong!")
    else:
        print("No, that doesn't work.")

def input_num():
    a = int(input("Choose a number for a: "))
    b = int(input("Choose a number for b: "))
    c = int(input("Choose c number for c: "))
    n = int(input("Choose a number for n: "))
    check_format(a, b, c, n)

input_num()


# EXERCISE 5.3: Check if three lengths could form a triangle or not
# if any of three lengths is greater than the two other, we can't form a triangle

def is_triangle(a, b, c):
    if (a > b + c) or (b > a + c) or (c > a + b):
        print("No")
    else:
        print("Yes")

def check_triangle():
    a = int(input("Choose a number for a: "))
    b = int(input("Choose a number for b: "))
    c = int(input("Choose c number for c: "))
    is_triangle(a, b, c)

check_triangle()


# EXERCISE 5.6.

import turtle
bob = turtle.Turtle()

def koch(turtle, length):
    if length < 3:
        turtle.fd(length)
        return
    koch(turtle, length/3)
    turtle.lt(60)
    koch(turtle, length/3)
    turtle.rt(120)
    koch(turtle, length/3)
    turtle.lt(60)
    koch(turtle, length/3)

def snowflake(turtle, length):
    for i in range(3):
        koch(turtle, length)
        turtle.rt(120)

koch(bob, 30)

bob.pu()
bob.fd(50)
bob.pd()

snowflake(bob, 30)

turtle.mainloop()
