import random

# Function to provide random message prompts with Game of Thrones references
def message_prompts():
    messages = [
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
    return random.choice(messages)  # Return a random message from the list

# Function to run a single game of guessing
def guessing_game(level):
    ranges = {1: 50, 2: 100, 3: 100}  # Different ranges for levels
    max_attempts = {1: 10, 2: 7, 3: 5}  # Different max attempts for levels
    hint_frequency = {1: 1, 2: 2, 3: 3}  # Hint frequency for levels (1: Every attempt, 2: Every 2 attempts, 3: Every 3 attempts)

    max_range = ranges.get(level, 50)
    secret_number = random.randint(1, max_range)
    attempts = 0

    print(f"\nLevel {level} - Guess the number between 1 and {max_range}")
    print(f"You have {max_attempts[level]} attempts to guess the number.")

    while attempts < max_attempts[level]:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < secret_number:
                if attempts % hint_frequency[level] == 0:
                    print("Too low! " + message_prompts())
                else:
                    print("Too low!")
            elif guess > secret_number:
                if attempts % hint_frequency[level] == 0:
                    print("Too high! " + message_prompts())
                else:
                    print("Too high!")
            else:
                print(f"\nCongratulations! You guessed it in {attempts} attempts!")
                return attempts

        except ValueError:
            print("Please enter a valid number.")
    
    print(f"\nYou've used all {max_attempts[level]} attempts. The number was {secret_number}.")
    return max_attempts[level]

# Main function to control the game flow
def game_of_guessing():
    print("Valar Morghulis")
    print("Welcome to the Game of Guessing!")
    print("The Lowest point wins")
    score = 0
    level = 1

    while level <= 3:
        score += guessing_game(level)
        
        if level < 3:
            continue_game = input("Do you want to continue to the next level? (yes/no): ").strip().lower()
            if continue_game != 'yes':
                break
        level += 1

    print(f"\nYour final score is {score} points!")
    print("\nValar Dohaeris")

if __name__ == "__main__":
    game_of_guessing()
input()