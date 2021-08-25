'''
11.2 Dictionary as a collection of counters
Suppose you are given a string and you want to count how many times each letter appears.

Approach 2: You could create a list with 26 elements. Then you could convert each character to
a number (using the built-in function ord), use the number as an index into the list,
and increment the appropriate counter.

'''

## If we count on each letter of the alphabet system
import string

# use string module to create a list of alphabet letters
def alphabet():
    l = string.ascii_lowercase
    l_list = []
    for i in l:
        l_list.append(i)
    return l_list


# how many times each letter appears
def letter_count(sentence, letter):
    count = 0
    for c in sentence:
        if ord(c) == ord(letter):
            count += 1
    return count


sentence = "No matter how difficult this exercise is, I will complete it."
alphabet_list = alphabet()

# count how many times each alphabet letter appears
for i in alphabet_list:
    print(i, letter_count(sentence.lower(), i))


    
## If we count only on each letter of the sentence:
def letter_count(sentence, letter):
    count = 0
    for c in sentence:
        if ord(c) == ord(letter):
            count += 1
    return count


sentence = "No matter how difficult this exercise is, I will complete it."

# count how many times each alphabet letter appears
for i in sentence:
    print(i, letter_count(sentence, i))


'''
Approach 3: You could create a dictionary with characters as keys and counters as the corresponding values. 
The first time you see a character, you would add an item to the dictionary.
After that you would increment the value of an existing item.
'''

## Use if

def histogram(s):
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d


h = histogram('brontosaurus')
print(h)

## Replace if with the method get
def histogram(s):
    d = dict()
    for c in s:
        d[c] = 1 + d.get(c, 0)
    return d


h = histogram('brontosaurus')
print(h)


# EXERCISE 11.1.
'''
Write a function that reads the words in words.txt and stores them as keys in a
dictionary. It doesn’t matter what the values are. Then you can use the in operator as a fast way to
check whether a string is in the dictionary.
If you did Exercise 10.10, you can compare the speed of this implementation with the list in operator
and the bisection search.
'''

def word_list():
    d = dict()
    fin = open('words.txt')
    for line in fin:
        word = line.strip()
        d[word] = 1
    return d


def check_word(d, word):
    return word in d


start_time = time.time()
word_list = word_list()
elapsed_time = time.time() - start_time

for word in {'aa': 1, 'alien': 1, 'allen': 1, 'zymurgy': 1}:
    print(word, 'in dictionary is', check_word(word_list, word))
print(elapsed_time, 'seconds')


# In operator in list and bisection search:

