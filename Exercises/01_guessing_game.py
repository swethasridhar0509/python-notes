import random 

while True:
    print("Number Guessing Game")
    print()

    level = input("Choose a Level (Easy, Medium, Hard): ").strip().lower()
    attempts = {"easy": 10, "medium": 7, "hard": 2}

    number = random.randint(1, 100)
    i = 1
    while i <= attempts[level]:
        try:
            guess = int(input("Enter Guess: "))
        except ValueError:
            print("Enter an integer")
        else:
            if 1 <= guess <= 100:
                
                if guess == number:
                    print(f"Congratulations! You guessed it in {i} attempts")
                    break
                elif guess > number:
                    print(f"Too High! Try Again. {attempts[level] - i} Attempts Left.")
                    i += 1
                else:
                    print(f"Too Low! Try Again. {attempts[level] - i} Attempts Left.")
                    i += 1
                
            else:
                print("Enter an integer between 1 and 100")
    else:
        print(f"Game Over! The number was {number}")   

    if input("Do you want to Play Again? (y/n): ").strip().lower() == "n":
        break
