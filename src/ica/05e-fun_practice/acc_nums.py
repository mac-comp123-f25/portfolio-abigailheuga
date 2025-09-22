def sum_range(start_val, end_val):
    cnt = 0     # initialize accumulator to default value 0
    for x in range(start_val, end_val + 1):
        cnt = cnt + x     # update: add new x value to old value of cnt
    return cnt

# Example of adding numbers in a range
print(sum_range(1,5))

# Start and end values passed in are the same number
print(sum_range(7,7))

# Start value is greater than the end value
print(sum_range(10,5))

# Both values are negative
print(sum_range(-3, -1))