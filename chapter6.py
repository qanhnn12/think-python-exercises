# EXERCISE 6.1: Draw a stack diagram for the following program.
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


# EXERCISE 6.2: Write a function named ack that evaluates the Ackermann function
def ack(m, n):
    if m == 0:
        return n+1
    elif m > 0 and n == 0:
        return ack(m-1, 1)
    else:
        return ack(m-1, ack(m, n-1))

print(ack(3, 4))

    
# EXERCISE 6.3
def first(word):
    return word[0]

def last(word):
    return word[-1]

def middle(word):
    return word[1:-1]

# return nothing when a string has equal or less than 2 letters
print(middle('hi'))
print(middle('i'))
print(middle(''))


# is_palindrome function that returns True if it is a palindrome and False otherwise
def is_palindrome(word):
    if len(word) < 1:
        return True
    elif first(word) != last(word):
        return False
    return is_palindrome(middle(word))

print(is_palindrome('mom'))
print(is_palindrome('bobby'))
print(is_palindrome('noon'))
print(is_palindrome('danger'))


# EXERCISE 6.4: Write a function called is_power that takes parameters a and b and returns True if a is a power of b
def is_divisible(x, y):
    """from section 6.4 textbook:
    return a boolean whether x is divisible by y
    x is divisible by y if the remainder when x is divided by y is 0
    """
    return x % y == 0


def is_power(a, b):
    """return a boolean whether a is a power of b
    a is a power of b if it is divisible by b and a/b is a power of b
    a and b must be positive integers"""

    # 1st base case: a=b, a is a power of a itself
    if a == b:
        return True
    # 2nd base case: b=1, the only positive integer that is a power of '1' is '1' itself
    elif b == 1:
        return False
    # call is_divisible() and call is_power() recursively
    else:
        return is_divisible(a, b) and is_power(a/b, b)


# print five test cases
print("is_power(10, 2) returns: ", is_power(10, 2))
print("is_power(27, 3) returns: ", is_power(27, 3))
print("is_power(1, 1) returns: ", is_power(1, 1))
print("is_power(10, 1) returns: ", is_power(10, 1))
print("is_power(3, 3) returns: ", is_power(3, 3))


# EXERCISE 6.5: The greatest common divisor (GMD)
def gcd(a, b):
    if a % b == 0:
        return b
    return gcd(b, a % b)
