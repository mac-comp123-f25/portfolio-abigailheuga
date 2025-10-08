def every_other(lst):
    result = []
    for i in range(0, len(lst), 2):
        result.append(lst[i])
    return result
print(every_other([10, 20, 30, 40, 50, 60]))

def sum_positive(numbers):
    total = 0
    for num in numbers:
        if num > 0:
            total += num
        return total

print(sum_positive([3, -1, 7, 0, -5, 10]))