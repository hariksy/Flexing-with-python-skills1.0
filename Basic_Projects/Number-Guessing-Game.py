import random

def get_comedic_message():
    messages = [
        "Winter is coming... but your guess was not the one.", 
        "A Lannister always pays his debts, but your guess wasn't quite right.",
        "You know nothing, Jon Snow... especially the number I'm thinking of.",
        "The night is dark and full of errors... like your guess.",
        "Valar Morghulis... but your guess was not the one to live.",
        "You must be as blind as Maester Aemon, for your guess was far from the mark.",
        "In the game of numbers, you win or you guess again.",
        "Dracarys! Your guess went up in flames.",
        "You may be the King in the North, but you're not the Guesser of the Number.", 
        "The North remembers... that your guess was incorrect.", 
        "When you play the number guessing game, you win or you die. Unfortunately, you didn't win this time.",
        "The things I do for love... do not include giving hints for your guess.",
        "I drink and I know things... but I don't know the number you guessed.", 
        "I am the sword in the darkness... but not the number in your guess.", 
        "The night's watch has ended for your guess."
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
