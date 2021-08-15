# Exercise 3.1. 

def right_justify(s):
    print(' '*(70 - len(s)) + s)

right_justify('monty')

# Exercise 3.2



# Exercise 3.3
'''
1. Write a function that draws a grid like the following:
+ - - - - + - - - - +
|         |         |
|         |         |
|         |         |
|         |         |
+ - - - - + - - - - +
|         |         |
|         |         |
|         |         |
|         |         |
+ - - - - + - - - - +
'''

def do_twice(f):
    f()
    f()

def do_four(f):
    do_twice(f)
    do_twice(f)

def border_row():
    print("+", "-" * 4, "+", "-" * 4, "+")

def border_col():
    print("|", " " * 4, "|", " " * 4, "|")

def half_grid():
    border_row()
    do_four(border_col)

def grid():
    do_twice(half_grid)
    border_row()

grid()


'''
2. Write a function that draws a similar grid with four rows and four columns.
+ ---- + ---- + ---- +
|      |      |      |
|      |      |      |
|      |      |      |
|      |      |      |
+ ---- + ---- + ---- +
|      |      |      |
|      |      |      |
|      |      |      |
|      |      |      |
+ ---- + ---- + ---- +
|      |      |      |
|      |      |      |
|      |      |      |
|      |      |      |
+ ---- + ---- + ---- +
'''

def do_twice(f):
    f()
    f()

def do_four(f):
    do_twice(f)
    do_twice(f)

def border_row():
    print("+", "-" * 4, "+", "-" * 4, "+", "-" * 4, "+")

def border_col():
    print("|", " " * 4, "|", " " * 4, "|", " " * 4, "|")

def border_grid():
    border_row()
    do_four(border_col)

def grid_four():
    do_twice(border_grid)
    border_row()
    do_four(border_col)
    border_row()

grid_four()
