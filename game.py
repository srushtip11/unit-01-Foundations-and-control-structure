number = 50

while True:

    guess = int(input("Enter your guess: "))

    if guess < number:
        print("Too Low")
    elif guess > number:
        print("Too High")
    else:
        print("Correct!")
        break
