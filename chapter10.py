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
        total += x
        t1.append(total)
    return t1



# EXERCISE 10.3.
'''
Write a function called middle that takes a list and returns a new list that contains
all but the first and last elements. For example:
>>> t = [1, 2, 3, 4]
>>> middle(t)
[2, 3]
'''

def middle(t):
    return t[1:-1]
    
    
    
# EXERCISE 10.4. 
'''
Write a function called chop that takes a list, modifies it by removing the first and
last elements, and returns None. For example:
>>> t = [1, 2, 3, 4]
>>> chop(t)
>>> t
[2, 3]
'''

# Approach 1: Use del
def chop(t):
    del t[0]
    del t[-1]
    return t

# Aproach 2: Use pop method
def chop(t):
    t.pop(0)
    t.pop(-1)
    return t



# EXERCISE 10.5.
'''
Write a function called is_sorted that takes a list as a parameter and returns True
if the list is sorted in ascending order and False otherwise. For example:
>>> is_sorted([1, 2, 2])
True
>>> is_sorted(['b', 'a'])
False
'''

def is_sorted(t):
    return t == sorted(t)



# EXERCISE 10.6.
'''
Two words are anagrams if you can rearrange the letters from one to spell the other.
Write a function called is_anagram that takes two strings and returns True if they are anagrams.
'''

def anagrams(a, b):
    return sorted(a) == sorted(b)



# EXERCISE 10.7.
'''
Write a function called has_duplicates that takes a list and returns True if there
is any element that appears more than once. It should not modify the original list.
'''

# Approach 1: Use count
def has_duplicates(t):
    for x in t:
        if t.count(x) > 1:
            return True
    return False

# Approach 2: Use sort and list slices 
def has_duplicates(t):
    t.sort()
    for i in range(len(t)-1):
        if t[i] == t[i+1]:
            return True
    return False

