def select_words(s, fn):
    matches = []

    file_in = open(fn, "r")

    for line in file_in:
        word = line.strip()
        if s in word:
            matches.append(word)

    file_in.close()

    return matches


#tests
print(len(select_words("ii", "../TextFiles/shortcross.txt")))      # should be 2
print(len(select_words("ii", "../TextFiles/crosswords.txt")))     # should be 38

print(len(select_words("quo", "../TextFiles/shortcross.txt")))    # should be 0
print(len(select_words("quo", "../TextFiles/crosswords.txt")))