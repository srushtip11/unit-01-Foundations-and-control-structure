n = int(input("Enter number: "))

sum = 0
product = 1

while n > 0:
    digit = n % 10
    sum = sum + digit
    product = product * digit
    n = n // 10

print("Sum =", sum)
print("Product =", product)
