# EXERCISE 9.1. 
# Write a program that reads words.txt, prints words with more than 20 Characters (not counting whitespace).
fin = open('words.txt')
for line in fin:
    word = line.strip()
    if len(word) > 20:
        print(word)

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
    if 'e' not in word:                         # or we could use the has_no_e function above: if has_no_e(word)
        no_e_count += 1
        print(word)
    total += 1

no_e_pct = no_e_count / total * 100
print(no_e_pct, 'percentage of words in the list that have no “e”.')


# EXERCISE 9.2


