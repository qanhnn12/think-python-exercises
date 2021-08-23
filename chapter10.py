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


# Create a list of random intergers from 1 to 365 as birthdays, with length n

def random_bdays(n):
    t = []
    for i in range(n):
        bday = random.randint(1, 365)
        t.append(bday)
    return t


# Given the number of students and number of simmulations, counts duplicates

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



# EXERCISE 10.9. 
'''
Write a function that reads the file words.txt and builds a list with one element
per word. Write two versions of this function, one using the append method and the other using
the idiom t = t + [x]. Which one takes longer to run? Why?
'''

# Approach 1: Use append method
import time
def word_list_1():
    fin = open('words.txt')
    t = []
    for line in fin:
        word = line.strip()
        t.append(word)
    return t

start_time = time.time()
t = word_list_1()
elapsed_time = time.time() - start_time

print(len(t))
print(t[:20])
print(elapsed_time, 'seconds')
## runtime = 0.04042410850524902 seconds


# Approach 2: Use the idiom t = t + [x]
import time

def word_list_2():
    fin = open('words.txt')
    t = []
    for line in fin:
        word = line.strip()
        t = t + [word]
    return t

start_time = time.time()
t = word_list_2()
elapsed_time = time.time() - start_time

print(len(t))
print(t[:20])
print(elapsed_time, 'seconds')
## runtime = 155.08912873268127 seconds



# EXERCISE 10.10.
'''
Write a function called in_bisect that takes a sorted list and a target value and returns True if
the word is in the list and False if it’s not.
'''

def word_list():
    fin = open('words.txt')
    t = []
    for line in fin:
        word = line.strip()
        t.append(word)
    t.sort()
    return t


def in_bisect(word_list, word):
    if len(word_list) == 0:
        return False

    # index of the word on the middle
    i = len(word_list) // 2

    if word_list[i] == word:
        return True

    if word_list[i] > word:
        # search the first half
        return in_bisect(word_list[:i], word)
    else:
        # search the second half
        return in_bisect(word_list[i+1:], word)

    
# Use the bisect module to perform bisection search
import bisect    
def in_bisect_cheat(word_list, word):
    i = bisect.bisect_left(word_list, word)
    if i == len(word_list):
        return False
    return word_list[i] == word


word_list = word_list()


# check the list using our function in_bisect():
for word in ['aa', 'alien', 'allen', 'zymurgy']:
    print(word, 'in list', in_bisect(word_list, word))

    
# check the list using the bisect module:
for word in ['aa', 'alien', 'allen', 'zymurgy']:
        print(word, 'in list', in_bisect_cheat(word_list, word))

        
        
# EXERCISE 10.11.

import bisect

def word_list():
    fin = open('words.txt')
    t = []
    for line in fin:
        word = line.strip()
        t.append(word)
    t.sort()
    return t


def in_bisect_cheat(word_list, word):
    i = bisect.bisect_left(word_list, word)
    if i == len(word_list):
        return False
    return word_list[i] == word


def reverse_pair(word_list, word):
    rv_word = word[::-1]
    return in_bisect_cheat(word_list, rv_word)


word_list = word_list()


for word in word_list:
    if reverse_pair(word_list, word):
        print(word, word[::-1])
