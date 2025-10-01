money = 732

print(f"Making change for {money} cents:")

dollars = money // 100
remainder = money % 100

quarters = remainder // 4
remainder = remainder % 25

dimes = remainder // 10
remainder = remainder % 10

nickels = remainder // 5
remainder = remainder % 5

pennies = remainder

print("Dollars:", dollars)
print("Quarters:", quarters)
print("Dimes:", dimes)
print("Nickels:", nickels)
print("Pennies:", pennies)