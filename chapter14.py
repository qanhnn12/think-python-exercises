# EXERCISE 14.1
def sed(pattern, replace, source, dest):
    fin = open(source, 'r')
    fout = open(dest, 'w')

    for line in fin:
        line = line.replace(pattern, replace)
        fout.write(line)

    fin.close()
    fout.close()

def main():
    pattern = "cant"
    replace = "can't"
    source = 'words.txt'
    dest = 'new_file.txt'
    sed(pattern, replace, source, dest)

if __name__ == '__main__':
    main()



# EXERCISE 14.2.

from anagram_sets import all_anagrams

# store the anagram dictionary in a “shelf”
def store_anagrams(filename):
    shelf = dict()
    d = all_anagrams(filename)
    for word, word_list in d.items():
        if len(word_list) > 1:
            shelf[word] = word_list
    return shelf

print(store_anagrams('words.txt'))


# look up a word and return a list of its anagrams
def read_anagrams(filename):
    t = []
    word = input("Enter a word you want to look up: ")
    anagrams = store_anagrams('words.txt')
    for k, v in anagrams.items():
        if k == word:
            for w in v:
                t.append(w)
        else:
            return 'That word is not in the list.'
    return t

print(read_anagrams('words.txt'))

