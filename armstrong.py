n = int(input("Enter number: "))

original = n
sum = 0

while n > 0:
    digit = n % 10
    sum = sum + digit * digit * digit
    n = n // 10

if sum == original:
    print("Armstrong Number")
else:
    print("Not Armstrong Number")
