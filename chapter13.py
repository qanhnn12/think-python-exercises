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


d = read_file('28500-8.txt')
print('Total number of words:', total_words(d))
print('Number of different words:', different_word(d))


'''
Exercise 13.3. Modify the program from the previous exercise to print the 20 most frequently used
words in the book.
'''

