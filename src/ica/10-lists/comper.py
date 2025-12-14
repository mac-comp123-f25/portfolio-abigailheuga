def times_n(n, numbers):
    return [n * x for x in numbers]

def remove_all(item, items):
    return [x for x in items if x != item]

if __name__ == '__main__':
    print(times_n(3, [1, 2, 3, 4]))
    print(remove_all(2, [1, 2, 3, 2, 4]))