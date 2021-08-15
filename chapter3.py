# Exercise 3.1. 
''' Write a function named right_justify that takes a string named s as a parameter 
and prints the string with enough leading spaces so that the last letter of the string is in column 70 of the display.'''

def right_justify(s):
    print(' '*(70 - len(s)) + s)

right_justify('monty')



# Exercise 3.2.

'''1. Type this example into a script and test it.'''

def do_twice(f):
    f()
    f()

def print_spam():
    print('spam')

do_twice(print_spam)


'''2. Modify do_twice so that it takes two arguments, a function object and a value, and calls the function twice, passing the value as an argument.'''

def do_twice(f, a):
   f(a)
   f(a)

def print_spam(word):
   print(word)

do_twice(print_spam, 'ss')


'''3. Copy the definition of print_twice from earlier in this chapter to your script.'''

def print_twice(bruce):
    print(bruce)
    print(bruce)

    
'''4. Use the modified version of do_twice to call print_twice twice, passing 'spam' as an argument.'''

do_twice(print_twice, 'spam')


'''5. Define a new function called do_four that takes a function object and a value and calls the function four times, passing the value as a parameter. 
There should be only two statements in the body of this function, not four.'''

def do_four(print_spam, arg):
    do_twice(print_spam, arg)
    do_twice(print_spam, arg)

do_four(print_twice, 'abc')
        
        
# Exercise 3.3.
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
