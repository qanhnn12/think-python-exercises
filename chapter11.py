# EXERCISE 11.1.

# Use dictionary: 0.058892011642456055 seconds

import time

def word_dict():
    d = dict()
    fin = open('words.txt')
    for line in fin:
        word = line.strip()
        
        # assign value for each key: 1
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


# Use bi_insect(): 0.05539584159851074 seconds



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
