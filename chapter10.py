# EXERCISE 10.1.

# Approach 1:
def nested_sum(t):
    total = 0
    for nest in t:
        total += sum(nest)
    return total
  
# Approach 2:
def nested_sum(t):
    k = []
    for l in t:
        for num in l:
            k.append(num)
    return sum(k)


# EXERCISE 10.2.

def cumsum(t):
    t1 = []
    total = 0
    for x in t:
        total += x
        t1.append(total)
    return t1



# EXERCISE 10.3.

def middle(t):
    return t[1:-1]
    
    
    
# EXERCISE 10.4. 

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

def is_sorted(t):
    return t == sorted(t)



# EXERCISE 10.6.

def is_anagrams(a, b):
    return sorted(a) == sorted(b)



# EXERCISE 10.7.

# Approach 1: Use count
def has_duplicates(t):
    for i in t:
        if t.count(i) > 1:
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

import random

def has_duplicates(t):
    t.sort()
    for i in range(len(t)-1):
        if t[i] == t[i+1]:
            return True
    return False


# Create a list of random integers from 1 to 365 as birthdays, with length n

def random_bdays(n):
    t = []
    for i in range(n):
        bday = random.randint(1, 365)
        t.append(bday)
    return t


# Counts duplicates based on the number of students and number of simulations

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
## runtime = 0.0628809928894043 seconds


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

    # divide the list into 2 parts
    i = len(word_list) // 2

    # if it coincidentally matches the word we wanna find
    if word_list[i] == word:
        return True

    elif word_list[i] > word:
        # search the first half
        return in_bisect(word_list[:i], word)
    else:
        # search the second half
        return in_bisect(word_list[i+1:], word)

    
# Use the bisect module to perform bisection search
import bisect    
def in_bisect_cheat(word_list, word):
    i = bisect.bisect_left(word_list, word)
    # base case: the list is empty or the word we wanna find doesn't in the list
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


# search the reversed word in the list using binary search
# return True if their is the reversed word
def reverse_pair(word_list, word):
    rv_word = word[::-1]
    return in_bisect_cheat(word_list, rv_word)


word_list = word_list()


for word in word_list:
    if reverse_pair(word_list, word):
        print(word, word[::-1])

        
 
# EXERCISE 10.12.
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

# Checks whether a word contains two interleaved words
def interlock(word_list, word):
    evens = word[::2]
    odds = word[1::2]
    return in_bisect_cheat(word_list, evens) and in_bisect_cheat(word_list, odds)

# Checks whether a word contains two interleaved words with 
# n is the number of interleaved words
def interlock_general(word_list, word, n):
    for i in range(n):
        inter = word[i::n]
        if not in_bisect_cheat(word_list, inter):
            return False
        return True


word_list = word_list()


for word in word_list:
    if interlock(word_list, word):
        print(word, word[::2], word[1::2])

        
for word in word_list:
    if interlock_general(word_list, word, 3):
        print(word, word[0::3], word[1::3], word[2::3])
