import random

def get_comedic_message():
    messages = [
        "Oh no, that's not it! Maybe try counting the number of fingers you have left.",
        "Close, but no cigar. Unless you have a cigar, then you're still just close.",
        "So close, yet so far. Like trying to touch your toes without bending your knees.",
        "Nope, not this time. Keep going, you're making me laugh!",
        "Not quite! If at first, you don't succeed, skydiving is not for you.",
        "Nope, try again! Remember, it's just you against the infinite abyss of numbers.",
        "Nope, not this time! If guessing were a sport, you'd be... well, you'd be playing this game.",
        "Not quite! Keep going, you're getting warmer. Unless you're standing next to a penguin.",
        "Nope, not yet! Keep guessing, and remember, even a broken clock is right twice a day.",
        "Nope, that's not it! If guessing were an art, you'd be... well, you'd still be guessing."
    ]
    return random.choice(messages)

def main():
    print("Welcome to the Hilarious Number Guessing Game!")
    print("I've selected a number between 1 and 100. Try to guess it!")
    print("Hint: It's not a negative number, but it might be positively challenging.")

    secret_number = random.randint(1, 100)
    attempts = 0

    while True:
        try:
            guess = int(input("\nEnter your guess: "))
            attempts += 1

            if guess < secret_number:
                print("Too low! " + get_comedic_message())
            elif guess > secret_number:
                print("Too high! " + get_comedic_message())
            else:
                print(f"\nCongratulations! You guessed it in {attempts} attempts!")
                break

        except ValueError:
            print("Please enter a valid number.")

    print("\nThanks for playing the Hilarious Number Guessing Game!")

if __name__ == "__main__":
    main()
