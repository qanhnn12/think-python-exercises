# EXERCISE 10.1.
'''
Write a function called nested_sum that takes a list of lists of integers 
and adds up the elements from all of the nested lists. For example:
>>> t = [[1, 2], [3], [4, 5, 6]]
>>> nested_sum(t)
21
'''

def nested_sum(t):
    total = 0
    for nest in t:
        total += sum(nest)
    return total
  

# EXERCISE 10.2.
'''
Write a function called cumsum that takes a list of numbers and returns the cumulative sum; 
that is, a new list where the ith element is the sum of the first i + 1 elements from the original list. 
For example:
>>> t = [1, 2, 3]
>>> cumsum(t)
[1, 3, 6]
'''

def cumsum(t):
    t1 = []
    total = 0
    for x in t:
        total = total + x
        t1.append(total)
    return t1

