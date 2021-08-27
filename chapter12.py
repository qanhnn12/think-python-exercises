# EXERCISE 12.1.

def histogram(s):
    # create a dictionary in which each item is a character-frequency pair
    d = dict()
    
    # set value = 1 by default
    # if c has already existed, increment it by 1
    for c in s:
        d[c] = 1 + d.get(c, 0)
    return d


def most_frequent(s):
    hist = histogram(s)

    # from the hist dictionary, create a list of tuples 
    # append the frequency-character (instead of character-frequency) tuples in the list
    # to sort the tuples in descending order of frequency
    
    t = []
    for c, freq in hist.items():
        t.append((freq, c))

    t.sort(reverse=True)

    # from the list of frequency-character tuples, take out the letters
    result = []
    for freq, c in t:
        result.append(c)

    return result


print(most_frequent('pneumonoultramicroscopicsilicovolcanoconiosis'))



# EXERCISE 12.2.
'''
1. Write a program that reads a word list from a file. 
Prints all the sets of words that are anagrams.
'''

# return a string that contains all letter in ascending order
def ordered_string(s):
    t = list(s)
    t.sort()
    t = ''.join(t)
    return t


# create a dictionary that maps from a collection of letters 
# to a list of words that can be spelled with those letters
def all_anagrams(filename):    
    d = dict()
    for line in open(filename):
        word = line.strip().lower()
        
        # t is a string that contains all letters
        # from which can form a word in the list
        t = ordered_string(word)
        
        if t not in d:
            d[t] = [word]
        else:
            d[t].append(word)
            

def anagram_sets(d):
    for v in d.values():
        
        # if each key has only 1 value, it doesn't have any anagram in the word list
        if len(v) > 1:
            print(v)
  

d = all_anagrams()
anagram_sets(d)
     


'''
2. Modify the previous program so that it prints the longest list of anagrams first, 
followed by the second longest, and so on.
'''
