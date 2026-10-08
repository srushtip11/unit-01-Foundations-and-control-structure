a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a > b and a > c:
    largest = a
elif b > c:
    largest = b
else:
    largest = c

if a < b and a < c:
    smallest = a
elif b < c:
    smallest = b
else:
    smallest = c

print("Largest =", largest)
print("Smallest =", smallest)
