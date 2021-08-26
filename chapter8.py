# EXERCISE 8.2
word = 'banana'
print(word.count('a'))

# EXERCISE 8.3
def is_palindrome(word):
    return word == word[::-1]
        
print(is_palindrome('iloveu'))
print(is_palindrome('noon'))

# EXERCISE 8.5.
word = str(input("Enter a string: "))
num = int(input("Enter a number: "))

def rotated_word(word, num):
    new_str = ''
    for letter in word:
        new_str = new_str + chr(ord(letter) + num)
    print(new_str)

rotated_word(word, num)
