def print_abbrev(file):
    file = open("../TextFiles/alice.txt", "r")
    for line in file:
      print(line[:20])
    file.close()

print_abbrev("../TextFiles/alice.txt")

