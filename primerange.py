start = int(input("Enter starting number: "))
end = int(input("Enter ending number: "))

count = 0

for n in range(start, end + 1):

    factors = 0

    for i in range(1, n + 1):
        if n % i == 0:
            factors = factors + 1

    if factors == 2:
        print(n)
        count = count + 1

print("Total Prime Numbers =", count)
