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

def is_anagrams(a, b):
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



# EXERCISE 10.8.
'''
If there are 23 students in your class, what are the chances that two of them have the same birthday?
You can estimate this probability by generating random samples of 23 birthdays and checking for matches
'''

import random


def has_duplicates(t):
    t.sort()
    for i in range(len(t)-1):
        if t[i] == t[i+1]:
            return True
    return False


# Create a list of random intergers from 1 to 365 as birthdays

def random_bdays(n):
    t = []
    for i in range(n):
        bday = random.randint(1, 365)
        t.append(bday)
    return t


# Generates a sample of birthdays and counts duplicates

def count_matches(num_students, num_simulations):
    count = 0
    for i in range(num_simulations):
        t = random_bdays(num_students)
        if has_duplicates(t):
            count += 1

    print('After %d simulations' % num_simulations)
    print('with %d students' % num_students)
    print('there were %d simulations with at least one match' % count)


count_matches(23, 1000)
