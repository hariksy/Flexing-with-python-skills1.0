import random  # Importing the random module to generate random numbers and select random messages

# Function to provide random message prompts with Game of Thrones references
def message_prompts():
    message = [
        "Winter is coming... but your guess was not the one.", 
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
        "You drink and you know things... but you don't know the number you guessed.", 
        "I am the sword in the darkness... but not the number in your guess.", 
    ]
    return random.choice(message)  # Return a random message from the list

# Main function for the Game of Guessing
def g_o_g():
    print("Valar Morghulis")
    print("Welcome to Game of Guessing!")
    print("I've selected a number between 1 and 100. Try to guess it!")
    print("In the Game of Guessing, either you win or you try again")
    print("Click Enter to Begin the Game of Guessing")
    input()  # Wait for the user to press Enter to start the game

    secret_number = random.randint(1, 100)  # Generate a random number between 1 and 100
    attempts = 0  # Initialize attempt counter

    while True:  # Start an infinite loop for guessing
        try:
            guess = int(input("Enter your guess: "))  # Get the user's guess as an integer
            attempts += 1  # Increment the attempt counter

            if guess < secret_number:  # Check if the guess is too low
                print("Too low! " + message_prompts())
            elif guess > secret_number:  # Check if the guess is too high
                print("Too high! " + message_prompts())
            else:
                print(f"\nCongratulations! You guessed it in {attempts} attempts!")  # Correct guess
                break  # Exit the loop

        except ValueError:  # Handle non-integer input
            print("Please enter a valid number.")

    print("\nThe night's watch has ended for your guess.")  # End of game message
    print("\nValar Dohaeris")  # Closing message

if __name__ == "__main__":
    g_o_g()  # Run the game function if the script is executed directly
input()  # Wait for user input before closing the program
