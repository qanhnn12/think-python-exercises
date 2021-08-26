def histogram(s):
    # create a dictionary in which each item is a character-frequency pair
    d = dict()
    for c in s:
        d[c] = 1 + d.get(c, 0)
    return d


def most_frequent(s):
    hist = histogram(s)

    # create a list of tuples from the hist dictionary
    # append the frequency-character tuple in the list
    # sort the tuple based on the frequency in descending order
    
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
