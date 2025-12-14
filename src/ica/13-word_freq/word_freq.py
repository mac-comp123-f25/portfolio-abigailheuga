import string


def compute_frequencies(filename):
    f = open(filename, 'r')
    text = f.read()
    f.close()

    clean_words = []
    words = text.split()
    for word in words:
        newWord = word.strip(string.punctuation)
        clean_words.append(newWord)
    print(clean_words)

    for w in clean_words:
        print(w)


compute_frequencies("../TextFiles/alice.txt")