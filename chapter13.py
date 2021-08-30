'''
Exercise 13.1. Write a program that reads a file, breaks each line into words, strips whitespace and
punctuation from the words, and converts them to lowercase.
'''

# create a dict in which each item shows how many times each word was used

import string

def read_file(filename):
    d = {}
    data = open(filename)
    
    # for each line in the data, replace the hyphen by the empty string
    for line in data:
        line = line.replace('-', ' ')

     # for each line in the data, replace the hyphen by the empty string
        for word in line.split():
            word = word.strip(string.punctuation + string.whitespace)
            word = word.lower()

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

# total number of words = sum of the frequencies of each word in the book
def total_words(d):
    return sum(d.values())


# the number of different words = the number of key-value pairs
def different_word(d):
    return len(d)


d = read_file('filename')
print('Total number of words:', total_words(d))
print('Number of different words:', different_word(d))



'''
Exercise 13.3. Modify the program from the previous exercise to print the 20 most frequently used
words in the book.
'''

def common_words(d):
    dc = []
    for word, freq in d.items():
        dc.append((freq, word))
    dc.sort(reverse=True)
    return dc


d = read_file('filename')
t = common_words(d)

print('The most common words are:')
for freq, word in t[:20]:
    print(word, freq, sep='\t')         # use the keyword argument sep to tell print to use a tab character as a “separator”
    
    
    
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

d1 = read_file('28500-8.txt')
d2 = read_file('words.txt')

diff = subtract(d1,d2)
print("Words in the books that are not in the word list are:")
for word in diff:
    print(word, end=' ')
