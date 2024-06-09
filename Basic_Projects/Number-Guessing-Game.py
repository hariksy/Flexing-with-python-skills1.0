import random

def message_prompts():
    messages = [
        "Winter is coming... but your guess was not the one.", 
        "A Lannister always pays his debts, but your guess wasn't quite right.",
        "You know nothing, Jon Snow... especially the number I'm thinking of.",
        "The night is dark and full of errors... like your guess.",
        "Valar Morghulis... but your guess was not the one to live.",
        "You must be as blind as Maester Aemon, for your guess was far from the mark.",
        "In the game of numbers, you win or you guess again.",
        "Dracarys! Your guess went up in flames.",
        "Hold the door... to let your next guess through, because that one was wrong.",
        "You may be the King in the North, but you're not the Guesser of the Number.", 
        "The North remembers... that your guess was incorrect.", 
        "When you play the number guessing game, you win or you die. Unfortunately, you didn't win this time.", 
        "A mind needs books as a sword needs a whetstone. Looks like you need to sharpen your guessing skills.",
        "The things I do for love... do not include giving hints for your guess.",
        "I drink and I know things... but I don't know the number you guessed.", 
        "I am the sword in the darkness... but not the number in your guess.", 
        "The night's watch has ended for your guess."
    ]
    return random.choice(messages)

def g_o_g():
    print("Welcome to Game of Guessing!")
    print("I've selected a number between 1 and 100. Try to guess it!")
    print("In the Game of Guessing, either you win or you try again")
    print("Click Enter to Begin the Game of Guessing")
    print()


    secret_number = random.randint(1, 100)
    attempts = 0

    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < secret_number:
                print("Too low! " + message_prompts())
            elif guess > secret_number:
                print("Too high! " + message_prompts())
            else:
                print(f"\nCongratulations! You guessed it in {attempts} attempts!")
                break

        except ValueError:
            print("Please enter a valid number.")

    print("\nThanks for playing the Game of Guessing!")
if __name__ == "__g_o_g__":
    g_o_g()
