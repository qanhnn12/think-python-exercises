# EXERCISE 8.2
word = 'banana'
print(word.count('a'))

# EXERCISE 8.3
def is_palindrome(word):
    if len(word) > 1 and word == word[::-1]:
        return True
    else:
        return False
        
print(is_palindrome('iloveu'))
print(is_palindrome('noon'))

# EXERCISE 8.4
word = str(input("Enter a string: "))
num = int(input("Enter a rotated number: "))

def rotate_word(word, num):
    new_str = ''
    for letter in word:
        new_str = new_str + chr(ord(letter) + num)
    print(new_str)

rotate_word(word, num)
