def sum_digits(words):
    total = 0
    for word in words:
        digits = [ch for ch in word if ch.isdigit()]
        if digits:
            num = int(digits[0] + digits[-1])
            total += num
    return total

print(sum_digits(['jaw2n5btf9w', 'xxgg7x']))
print(sum_digits(['comp123', '1600grand', 'spring24']))