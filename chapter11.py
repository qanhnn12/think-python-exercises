# EXERCISE 11.1. 

import bisect
import time


def word_list():
    fin = open('words.txt')
    t = []
    for line in fin:
        word = line.strip()
        t.append(word)
    t.sort()
    return t

def check_list(word_list, word):
    return word in word_list


def in_bisect_cheat(word_list, word):
    i = bisect.bisect_left(word_list, word)
    if i == len(word_list):
        return False
    return word_list[i] == word


def word_dict():
    fin = open('words.txt')
    d = dict()
    for line in fin:
        word = line.strip()
        d[word] = 1
    return d


def check_dict(word_dict, word):
    return word in word_dict


# runtime for list with in operator: 
start_time_list = time.time()
check_list(word_list(), 'hallo')
elapsed_time_list = time.time() - start_time_list
print('For list with in operator:', elapsed_time_list, 'seconds')


# runtime for list with binary search
start_time_bi = time.time()
in_bisect_cheat(word_list(), 'hallo')
elapsed_time_bi = time.time() - start_time_bi
print('For list with binary search:', elapsed_time_bi, 'seconds')


# runtime for dictionary with in operator
start_time_dict = time.time()
check_dict(word_dict(), 'hallo')
elapsed_time_dict = time.time() - start_time_dict
print('For dictionary with in operator:', elapsed_time_dict, 'seconds')


"""
For list with in operator: 0.09282755851745605 seconds
For list with binary search: 0.056894779205322266 seconds
For dictionary with in operator: 0.06388330459594727 seconds
"""


# EXERCISE 11.2.

def invert_dict(d):
    inverse = dict()
    for key in d:
        val = d[key]
        
        # create an empty list as the value of the inverse dict
        # append (the key of d as) the value into the inverse dict
        inverse.setdefault(val, []).append(key)
    return inverse

d = {'a': 0, 'b': 1, 'c': 1, 'd': 2}
print(invert_dict(d))



# EXERCISE 11.3.

cache = {}


def ack(m, n):
    if m == 0:
        return n+1
    elif m > 0 and n == 0:
        return ack(m-1, 1)

    # check if (m,n) exists in cache
    if (m, n) in cache:
        return cache[m, n]
    else:
        cache[m, n] = ack(m-1, ack(m, n-1))
        return cache[m, n]


print(ack(3, 4))
print(ack(3, 6))



# EXERCISE 11.4.

d = {}

def has_duplicates(t):
    for x in t:
        
        # if x is a key in dict, it can't be dupplicated
        if x in d:
            return True
        # append the value into d (we can skip this step if we don't care about d)
        d[x] = True
    return False

t = [1,2,3,4]
print(has_duplicates(t))

t.append(1)
print(has_duplicates(t))

print(d)



# EXERCISE 11.5.

def word_dict():
    d = dict()
    fin = open('words.txt')
    for line in fin:
        word = line.strip()
        d[word] = 1
    return d


# This function is taken from exercise 8.5
def rotated_word(word, num):
    new_str = ''
    for letter in word:
        new_str = new_str + chr(ord(letter) + num)
    return new_str


def rotate_pairs(word, word_dict):
    # there are 26 alphabet letters, so the maximum rotated range is 13
    for num in range(1, 14):
        rotated = rotated_word(word, num)
        if rotated in word_dict:
            print(word, num, rotated)

            
word_dict = word_dict()

for word in word_dict:
    rotate_pairs(word, word_dict)
