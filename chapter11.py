# EXERCISE 11.1.

# Use dictionary: 0.058892011642456055 seconds

import time

def word_dict():
    d = dict()
    fin = open('words.txt')
    for line in fin:
        word = line.strip()
        
        # assign value for each key is 1
        d[word] = 1
    return d


def check_word(d, word):
    return word in d


start_time = time.time()
word_dict = word_dict()
elapsed_time = time.time() - start_time

print(check_word(word_dict, 'swear'))
print(elapsed_time, 'seconds')


# Use in operator: 0.04341888427734375 seconds

import time

def word_list():
    fin = open('words.txt')
    t = []
    for line in fin:
        word = line.strip()
        t.append(word)
    return t

def check_word(word_list, word):
    for w in word_list:
        if word == w:
            return True
    return False

start_time = time.time()
word_list = word_list()

print(check_word(word_list, 'swear'))
elapsed_time = time.time() - start_time

print(elapsed_time, 'seconds')


# Use bi_insect() function: 0.05539584159851074 seconds


# EXERCISE 11.2.

def invert_dict(d):
    inverse = dict()
    for key in d:
        val = d[key]
        
        # create an empty list as the value 
        # then append (the key of d as) the value into inverse
        inverse.setdefault(val, []).append(key)
    return inverse

d = {'a': 0, 'b': 1, 'c': 1, 'd': 2}

print(invert_dict(d))

# EXERCISE 11.3.
