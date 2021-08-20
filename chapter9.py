# EXERCISE 9.1. 
# Write a program that reads words.txt, prints words with more than 20 Characters (not counting whitespace).
fin = open('words.txt')
for line in fin:
    word = line.strip()
    if len(word) > 20:
        print(word)

EXERCISE 9.2

