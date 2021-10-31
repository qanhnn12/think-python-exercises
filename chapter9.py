# EXERCISE 9.1. 
# Write a program that reads words.txt, prints words with more than 20 Characters (not counting whitespace).

def read_word():
    fin = open('words.txt')
    for line in fin:
        word = line.strip()
        if len(word) > 20:
            print(word)

read_word()


        
# EXERCISE 9.2.
# Write a function called has_no_e that returns True if the given word doesn’t have the letter “e” in it.

def has_no_e(word):
    for i in word:
        if i == 'e':
            return False
    return True

print(has_no_e('aespa'))


# Write a program that reads words.txt and prints only the words that have no “e”
# Compute the percentage of words in the list that have no “e”.

def pct_no_e():
    fin = open("words.txt")
    total = 0
    no_e_count = 0

    for line in fin:
        word = line.strip()
        if 'e' not in word:                         # or use the has_no_e function above: if has_no_e(word)
            no_e_count += 1
            print(word)
        total += 1

    no_e_pct = no_e_count / total * 100
    print(no_e_pct, 'percent of words in the list that have no “e”.')

pct_no_e()



# EXERCISE 9.3.
# Write a function named avoids that takes a word and a string of forbidden letters,
# and that returns True if the word doesn’t use any of the forbidden letters.

def avoids(word, forbids):
    for c in word:
        if c in forbids:
            return False
    return True

# Write a program that prompts the user to enter a string of forbidden letters
# and then prints the number of words that don’t contain any of them

def read_file():
    forbids = input('Enter a string of forbidden letters: ')
    fin = open('words.txt')
    count = 0
    for line in fin:
        word = line.strip()
        for c in word:
            if avoids(word, forbids):
                count += 1
    print("The number of words that don't contain any forbidden letters:", count)

read_file()



# EXERCISE 9.4. 
# Write a function named uses_only that takes a word and a string of letters, 
# and that returns True if the word contains only letters in the list

def uses_only(word, available):
    for letter in word:
        if letter not in available:
            return False
    return True



# EXERCISE 9.5.
# Write a function named uses_only that takes a word and a string of letters, 
# and that returns True if the word contains only letters in the list

# Approach 1:
def uses_all(word, required):
    for letter in required:
        if letter not in word:
            return False
    return True

# Approach 2:
def uses_all(word, required):
    return uses_only(required, word)


# How many words are there that use all the vowels aeiou? How about aeiouy?

fin = open('words.txt')
required = 'aeiou'
count = 0

for line in fin:
    word = line.strip()
    if uses_all(word, required):
        count += 1
print(count)



# EXERCISE 9.6.
# Write a function called is_abecedarian that returns True 
# if the letters in a word appear alphabetically (double letters are ok). 
# How many abecedarian words are there?

# Approach 1. Use for loop

def is_abecedarian(word):
    previous = word[0]
        for c in word:
            if c < previous:
                return False
            previous = c
        return True
    
# Approach 2. Use recursion

def is_abecedarian(word):
    if len(word) <= 1:
        return True
    if word[0] > word[1]:
        return False
    return is_abecedarian(word[1:])

# Approach 3. Use while loop

def is_abecedarian(word):
    i = 0
    while i < len(word)-1:
        if word[i+1] < word[i]:
            return False
        i = i+1
    return True



# EXERCISE 9.7.
# This question is based on a Puzzler (http://www.cartalk.com/content/puzzlers):

def check_triple_pairs(word):
    i = 0
    count = 0
    while i < len(word)-1:
        if word[i] == word[i+1]:
            count += 1
            if count == 3:
                return True
            i += 2
        else:
            i += 1
            count = 0
    return False

def find_triple_pairs():
    fin = open("words.txt")
    for line in fin:
        word = line.strip()
        if check_triple_pairs(word):
            print(word)

find_triple_pairs()



# EXERCISE 9.8.

def palindrome():
    for i in range(100000, 1000000):
        if str(i)[2:6] == str(i)[6:1:-1]:                  # last 4 digits
            i += 1
            if str(i)[1:6] == str(i)[5:0:-1]:              # last 5 digits
                i += 1
                if str(i)[1:5] == str(i)[4:0:-1]:          # 4 middle digits
                    i += 1
                    if str(i) == str(i)[::-1]:             # all 6 digits
                        print(i-3)                         # i-3 because we have incremented i by 1 after each set of if statement
palindrome()
