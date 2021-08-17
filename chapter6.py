# Exercise 6.1 - Draw a stack diagram for the following program. What does the program print?
def b(z):
    prod = a(z, z)
    print(z, prod)
    return prod

def a(x, y):
    x = x + 1
    return x * y

def c(x, y, z):
    total = x + y + z
    square = b(total)**2
    return square

x = 1
y = x + 1
print(c(x, y+3, x+y))

'''
main:
    x ---> 1
    y ---> 2
c:
    x ---> 1
    y ---> 5
    z ---> 3
    total ---> 9
    square ---> 8100
b:
    z ---> 9
    prod ---> 90
a:
    x ---> 9
    y ---> 9
    x ---> 10
 
Program prints:
9 90
8100   
'''


# Exercise 6.2 - Write a function named ack that evaluates the Ackermann function
def ack(m,n):
    if m == 0:
        return n+1
    elif m > 0 and n == 0:
        return ack(m-1, 1)
    else:
        return ack(m-1, ack(m, n-1))

# Exercise 6.3
# return the first character of a string
def first(word):
    return word[0]

# return the last character of a string
def last(word):
    return word[-1]

# return the middle characters of a string, except the first and last ones
def middle(word):
    return word[1:-1]

# is_palindrome function that returns True if it is a palindrome and False otherwise
def is_palindrome(word):
    if len(word) > 1 and first(word) == last(word):
        return True
    else:
        return False
    return is_palindrome(middle(word))

print(is_palindrome('mom'))
print(is_palindrome('bobby'))
print(is_palindrome('noon'))
print(is_palindrome('danger'))


# Exercise 6.4 - Write a function called is_power that takes parameters a and b and returns True if a is a power of b
def is_power(a, b):
    c = a / b
    if a % b == 0 and c % b == 0:
        return True
    else:
        return False

print(is_power(2, 5))


# Exercise 6.5 - The greatest common divisor (GMD)
def gcd(a, b):
    if a % b == 0:
        return b
    return gcd(b, a % b)
