def i_words(filename):
    file_in = open(filename, 'r')
    text = file_in.read()
    file_in.close()
    words = text.split()
    words_with_i = []

    for word in words:
        if 'i' in word:
            words_with_i.append(word)

    return words_with_i


print(i_words("../TextFiles/alice.txt"))
