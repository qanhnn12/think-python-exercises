# EXERCISE 12.1.

def histogram(s):
    # Map each letter to number of times it appears in s
    d = dict()
    for c in s:
        d[c] = 1 + d.get(c, 0)
    return d

def most_frequent(s):
    h = histogram(s)
    t = []

    # from the h dictionary, create a list of tuples 
    # append the frequency-letter (inst.of letter-frequency) tuples in the list
    # to sort the tuples in descending order of frequency

    for freq, letter in h.items():
        t.append((freq, letter))
    t.sort(reverse=True)
    
    # for each tuple in the list, print each freq-letter out
    
    for freq, letter in t:
        print(freq, letter)

most_frequent('pneumonoultramicroscopicsilicovolcanoconiosis')



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


# find all anagrams in the list of words
def all_anagrams():
    d = dict()
    for line in open('words.txt'):
        word = line.strip().lower()
        t = ordered_string(word)

        # t is a collection of letters
        # from which can form a word in the list
        if t not in d:
            d[t] = [word]
        else:
            d[t].append(word)
    return d


def anagram_sets(d):
    for v in d.values():
        
        # if each key has only 1 value,
        # it doesn't have any anagram in the word list
        if len(v) > 1:
            print(v)
  

d = all_anagrams()
anagram_sets(d)
     

'''
2. Modify the previous program so that it prints the longest list of anagrams first, 
followed by the second longest, and so on.
'''

# replace the anagram_sets() by this function
def anagram_sets_length_desc(d):
    t = []
    for v in d.values():
        if len(v) > 1:
            t.append((len(v),v))
    t.sort(reverse=True)

    # print the length and lists of anagrams
    for x in t:
        print(x)

        
d = all_anagrams()
anagram_sets_length_desc(d)


'''
3. In Scrabble a “bingo” is when you play all seven tiles in your rack, along with a letter on
the board, to form an eight-letter word. What collection of 8 letters forms the most possible
bingos? 
'''

# Select only the words in d that have 8 letters
def filter_length(d):
    res = {}
    for word, anagrams in d.items():
        if len(word) == 8:
            res[word] = anagrams
    return res


d = all_anagrams()
anagram_sets_length_desc(filter_length(d))



# EXERCISE 12.3.

# if there are only 2 differences between two words, they are metathesis_pairs
def word_diff(word1, word2):
    count = 0
    for c1, c2 in zip(word1, word2):
        if c1 != c2:
            count += 1
    return count


def metathesis_pairs(d):
    for anagrams in d.values():
        for word1 in anagrams:
            for word2 in anagrams:
                if word1 < word2 and word_diff(word1, word2) == 2:
                    print(word1, word2)


metathesis_pairs(all_anagrams())
