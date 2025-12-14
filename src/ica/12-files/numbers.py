def write_to_n(n, filename):
    outFile = open(filename, "w")

    for num in range(1, n + 1):
        outFile.write(str(num) + '\n')

    outFile.close()

write_to_n(5, "../TextFiles/numbers.txt")