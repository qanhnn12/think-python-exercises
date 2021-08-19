# EXERCISE 7.1
import math
from decimal import Decimal

# Newton's method to compute square root of a number
def mysqrt(a, x):
    while True:
        est_sqrt = (x + a/x) / 2.0
        if est_sqrt == x:
            break
        x = est_sqrt
    return x

print(mysqrt(4, 3))

# Use sqrt function in math to compute square root
def actual_square_method(a):
    return math.sqrt(a)

# Write a function to create a table like this:
'''
a   mysqrt(a)     math.sqrt(a)  diff
-   ---------     ------------  ----
1.0 1.0           1.0           0.0
2.0 1.41421356237 1.41421356237 2.22044604925e-16
3.0 1.73205080757 1.73205080757 0.0
4.0 2.0           2.0           0.0
5.0 2.2360679775  2.2360679775  0.0
6.0 2.44948974278 2.44948974278 0.0
7.0 2.64575131106 2.64575131106 0.0
8.0 2.82842712475 2.82842712475 4.4408920985e-16
9.0 3.0           3.0           0.0
'''

def test_square_root():
    a = 1
    x = 4
    while a < 10:                                               # use a while loop to increment a by 1 (a < 10, as showned in the table)
        y = Decimal(format(mysqrt(a, x), ".10f"))               # the Decimal built-in function has a default precision of 28 places, while the float has 18 places
        square_method = Decimal(format(math.sqrt(a), ".10f"))   # use format function with ".10f" to round to 10 decimal numbers
        diff = f'{(y - square_method):.10f}'                    # another way to round to 10 decimal numbers
        print(a, "\t", y, "\t", square_method, "\t", diff)      # "\t" is a tab
        a = a + 1

test_square_root()


# EXERCISE 7.2
def eval_loop():
    while True:
        prompt = input("Write a math equation: ")
        if prompt == "done":
            break
        else:
            new_prompt = eval(prompt)
            print(new_prompt)
    return eval(prompt)

eval_loop()


# EXERCISE 7.3
import math

# factorial function in chapter 6: part 6.5
def factorial(n):                                               
    if n == 0:
        return 1
    else:
        recurse = factorial(n-1)
        result = n * recurse
        return result

# function to calculate pi using Srinivasa Ramanujan's formula
def estimate_pi():                                              
    total = 0
    k = 0
    fact = (2*math.sqrt(2))/9801                        
    while True:
        num = factorial(4*k) * (1103 + 26390*k)                 # the numerator in the second fraction
        den = factorial(k)**4 * 396**(4*k)                      # the denominator in the second fraction
        term = fact * num / den
        total = total + term                                

        if abs(term) < 1e-15:                                   # calculate until the summation of term is smaller than 1e-15
            break
        k = k + 1
    return 1 / total

print(estimate_pi())

 # function to compare the above result with math.pi
def check_pi():                                                
    a = math.pi
    print(a)

print(check_pi())
