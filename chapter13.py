'''
Exercise 13.1. Write a program that reads a file, breaks each line into words, strips whitespace and
punctuation from the words, and converts them to lowercase.
'''

import string


def read_file(filename):
    d = {}
    data = open(filename)
    for line in data:
        line = line.replace('-', ' ')

        for word in line.split():
            word = word.strip(string.punctuation + string.whitespace)
            word = word.lower()

            d[word] = d.get(word, 0) + 1
    return d
  
  
  
