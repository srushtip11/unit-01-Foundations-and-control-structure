while True:

    print("\n1. Prime")
    print("2. Palindrome")
    print("3. Armstrong")
    print("4. Factorial")
    print("5. Fibonacci")
    print("6. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:

        n = int(input("Enter number: "))
        count = 0

        for i in range(1, n + 1):
            if n % i == 0:
                count = count + 1

        if count == 2:
            print("Prime")
        else:
            print("Not Prime")

    elif choice == 2:

        n = int(input("Enter number: "))
        original = n
        reverse = 0

        while n > 0:
            digit = n % 10
            reverse = reverse * 10 + digit
            n = n // 10

        if original == reverse:
            print("Palindrome")
        else:
            print("Not Palindrome")

    elif choice == 3:

        n = int(input("Enter number: "))
        original = n
        sum = 0

        while n > 0:
            digit = n % 10
            sum = sum + digit * digit * digit
            n = n // 10

        if sum == original:
            print("Armstrong")
        else:
            print("Not Armstrong")

    elif choice == 4:

        n = int(input("Enter number: "))
        fact = 1

        for i in range(1, n + 1):
            fact = fact * i

        print("Factorial =", fact)

    elif choice == 5:

        n = int(input("Enter number of terms: "))

        a = 0
        b = 1

        for i in range(n):
            print(a, end=" ")
            c = a + b
            a = b
            b = c

        print()

    elif choice == 6:

        print("Program Ended")
        break

    else:
        print("Invalid Choice")
