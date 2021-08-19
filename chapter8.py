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
