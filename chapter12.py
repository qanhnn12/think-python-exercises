def histogram(s):
    # create a dictionary in which each item is a character-frequency pair
    d = dict()
    for c in s:
        d[c] = 1 + d.get(c, 0)
    return d


def most_frequent(s):
    hist = histogram(s)

    # from the hist dictionary, create a list of tuples 
    # append the frequency-character (instead of character-frequency) tuples in the list
    # to sort the tuples based on the frequency in descending order
    
    t = []
    for c, freq in hist.items():
        t.append((freq, c))

    t.sort(reverse=True)

    # create a list of letters in decreasing order of frequency
    result = []
    for freq, c in t:
        result.append(c)

    return result

print(most_frequent('pneumonoultramicroscopicsilicovolcanoconiosis'))
