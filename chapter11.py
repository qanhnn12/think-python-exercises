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

