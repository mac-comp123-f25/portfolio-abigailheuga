def end_point(numbers):
    return (min(numbers), max(numbers))

# Test call 1
nums = [4,1,9,7,2,5]
result = end_point(nums)
print(result)

# Test call 2
low, high = end_point(nums)
print("Min:", low)
print("Max:", high)