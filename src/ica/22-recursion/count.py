def countdown(n):
    if n == 0:
        print("Blast Off!")
    else:
        print(n)
        countdown(n - 1)

# testing the code
countdown(5)

# trying the code with user input
n = int(input("Enter a number: "))
countdown(n)

# ^note that you need to comment out line 9 in order for the user input code to work