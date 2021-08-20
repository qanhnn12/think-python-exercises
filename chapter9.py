# EXERCISE 9.1. 
# Write a program that reads words.txt, prints words with more than 20 Characters (not counting whitespace).
fin = open('words.txt')
for line in fin:
    word = line.strip()
    if len(word) > 20:
        print(word)

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
print(no_e_pct, 'percentage of words in the list that have no “e”.')


# EXERCISE 9.3.
# Write a function named avoids that takes a word and a string of forbidden letters,
# and that returns True if the word doesn’t use any of the forbidden letters.
def avoid(word, forb):
    for i in word:
        if i == forb:
            return False
    return True

# Write a program that prompts the user to enter a string of forbidden letters
# and then prints the number of words that don’t contain any of them

fin = open('words.txt')
forb = str(input("Enter a string of forbidden letter: "))
count = 0

for line in fin:
    word = line.strip()
    if forb not in word:                        # or use the has_no_e function above: if avoid(word, forb)
        count += 1
print(count)

# EXERCISE 9.4. 
# Write a function named uses_only that takes a word and a string of letters, 
# and that returns True if the word contains only letters in the list
def uses_only(word, available):
    for letter in word:
        if letter not in available:
            return False
        return True
    
# EXERCISE 9.5.
# Write a function named uses_only that takes a word and a string of letters, and
# that returns True if the word contains only letters in the list
def uses_all(word, required):
    for letter in required:
        if letter not in word:
            return False
        return True

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
