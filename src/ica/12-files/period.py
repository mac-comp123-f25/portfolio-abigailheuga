def up_to_period(filename):
    file_in = open("../TextFiles/mockingbird.txt", 'r')
    text = file_in.read()
    file_in.close()
    result = ""

    for char in text:
        result += char
        if char == '.':
            break

    return result

print(up_to_period("../TextFiles/mockingbird.txt"))