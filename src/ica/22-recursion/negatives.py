def count_negatives(n):
    if len(n) == 0:
        return 0
    else:
        first = n[0]
        rest_count = count_negatives(n[1:])

        if first < 0:
            return 1 + rest_count
        else:
            return rest_count

# testing the code
print(count_negatives([3, -1, 7, -5, 0]))
print(count_negatives([]))
print(count_negatives([-1, -2, -3]))