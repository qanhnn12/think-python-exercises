'''
Exercise 13.1. Write a program that reads a file, breaks each line into words, strips whitespace and
punctuation from the words, and converts them to lowercase.
'''

import string

# create a dict in which each item shows how many times each word was used
def read_file(filename, skip_header):
    d = {}
    data = open(filename)

    # skip the header
    if skip_header:
        for line in data.readline():
            if line.startswith('***START OF THIS'):
                break
                
    # read the file until it reaches the end
    for line in data:
        if line.startswith('***END OF THIS'):
            break

    # for each line in the data, replace hyphens with spaces
        line = line.replace('-', ' ')

        # for each word in the list, remove punctuation and whitespace, and convert to lowercase
        for word in line.split():
            word = word.strip(string.punctuation + string.whitespace)
            word = word.lower()

            # map from word to frequency
            d[word] = d.get(word, 0) + 1
    return d
  
    
    
  '''
Exercise 13.2. Go to Project Gutenberg (http: // gutenberg. org ) and download your favorite
out-of-copyright book in plain text format.
Modify your program from the previous exercise to read the book you downloaded, skip over the
header information at the beginning of the file, and process the rest of the words as before.
Then modify the program to count the total number of words in the book, and the number of times
each word is used.
Print the number of different words used in the book. Compare different books by different authors,
written in different eras. Which author uses the most extensive vocabulary?
'''

# total number of words = sum of the frequencies in the book
def total_words(d):
    return sum(d.values())


# total number of DIFFERENT words = the number of key-value pairs
def different_word(d):
    return len(d)


d = read_file(filename)
print('Total number of words:', total_words(d))
print('Number of different words:', different_word(d))



'''
Exercise 13.3. Modify the program from the previous exercise to print the 20 most frequently used
words in the book.
'''

# Approach 1: Use dictionary and tuples

def common_words(d):
    common = []
    for word, freq in d.items():
        common.append((freq, word))
    common.sort(reverse=True)
    return common


d = read_file(filename)
t = common_words(d)

print('The most common words are:')
for freq, word in t[:20]:
    print(word, freq, sep='\t')         # use the keyword argument sep to tell print to use a tab character as a “separator”
    
    
    
# Approach 2: Use sorted
def common_words(d):
    common = sorted(d.items(), key=lambda item: item[1], reverse=True)
    return common


d = read_file(filename)
t = common_words(d)

print('The most common words are:')
for word, freq in t[:20]:
    print(word, freq, sep='\t')



'''
Exercise 13.4. Modify the previous program to read a word list (see Section 9.1) and then print all
the words in the book that are not in the word list. How many of them are typos? How many of
them are common words that should be in the word list, and how many of them are really obscure?
'''

def subtract(d1, d2):
    res = dict()
    for key in d1:
        if key not in d2:
            res[key] = None
    return res


d1 = read_file(filename1)
d2 = read_file(filename2)

diff = subtract(d1,d2)
print("Words in the books that are not in the word list are:")

for word in diff:
    print(word, end=' ')

    
    
'''
Exercise 13.5. Write a function named choose_from_hist that takes a histogram as defined in
Section 11.2 and returns a random value from the histogram, chosen with probability in proportion
to frequency. For example, for this histogram:
>>> t = ['a', 'a', 'b']
>>> hist = histogram(t)
>>> hist
{'a': 2, 'b': 1}
your function should return 'a' with probability 2/3 and 'b' with probability 1/3.
'''

def histogram(s):
    d = dict()
    for c in s:
        d[c] = 1 + d.get(c, 0)
    return d


def choose_from_hist(h):
    random_key = random.choice(list(h.keys()))
    probability = h[random_key] / sum(h.values())
    print('Random value is "{}" and its probability is {}/{}, i.e. {}.' \
          .format(random_key, h[random_key], sum(h.values()), probability))


d = read_file(filename)
h = histogram(d)
choose_from_hist(h)



'''
Exercise 13.6. Use set to write a program that uses set subtraction to find words
in the book that are not in the word list.
'''

# another way to do the exercise 13.4
def subtract(d1, d2):
    return set(d1) - set(d2)



'''
Exercise 13.7. Use an alternate way to write a program that to choose a random word from the book.

An alternative is:
1. Use keys to get a list of the words in the book.
2. Build a list that contains the cumulative sum of the word frequencies (see Exercise 10.2). 
The last item in this list is the total number of words in the book, n.
3. Choose a random number from 1 to n. Use a bisection search (See Exercise 10.10) to
find the index where the random number would be inserted in the cumulative sum.
4. Use the index to find the corresponding word in the word list
'''

import random
from bisect import bisect


def random_word(d):
    words = []
    freqs = []
    total_freq = 0

    # make a list of words and a list of cumulative frequencies
    for word, freq in d.items():
        total_freq += freq
        words.append(word)
        freqs.append(freq)

    # choose a random value and find its location in the cumulative list
    x = random.randint(0, total_freq-1)
    index = bisect(freqs, x)
    return words[index]


d = read_file(filename)

print("\n\nHere are some random words from the book")
    for i in range(100):
        print(random_word(d), end=' ')
