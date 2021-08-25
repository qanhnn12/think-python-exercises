'''
11.2 Dictionary as a collection of counters
Suppose you are given a string and you want to count how many times each letter appears.

Approach 2: You could create a list with 26 elements. Then you could convert each character to
a number (using the built-in function ord), use the number as an index into the list,
and increment the appropriate counter.

'''

## If we count on each letter based on the alphabet system
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

# count how many times each alphabet letter appears in a given sentence
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

# count how many times each alphabet letter in the sentence appears
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
