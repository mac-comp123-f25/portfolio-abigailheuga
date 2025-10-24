def compute_frequencies(filename):
    with open(filename, 'r') as f:
        contents = f.read()
    print(contents)

compute_frequencies("../TextFiles/alice.txt")