import random
import string
import pyperclip

print("Welcome to the drowssaP rotareneG")
print("\U0001F600")
DEFAULT_LENGTH = 12

#Generate a random password
def generate_password(length=DEFAULT_LENGTH, include_uppercase=False, include_numbers=False, include_special_chars=False):
    characters = string.ascii_lowercase
    if include_uppercase:
        characters += string.ascii_uppercase
    if include_numbers:
        characters += string.digits
    if include_special_chars:
        characters += string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

#Generate a password based on a given pattern
def generate_password_with_pattern(pattern):
    password = ''
    for char in pattern:
        if char == 'u':
            password += random.choice(string.ascii_uppercase)
        elif char == 'l':
            password += random.choice(string.ascii_lowercase)
        elif char == 'd':
            password += random.choice(string.digits)
        elif char == 's':
            password += random.choice(string.punctuation)
        else:
            password += char
    return password

#Generate a password based on personal information
def generate_password_with_personal_info(name, birthdate):
    password = name[:3] + birthdate[-4:]
    return password

#Export passwords to a file
def export_passwords(passwords):
    with open('passwords.txt', 'w') as file:
        for password in passwords:
            file.write(password + '\n')
    print("Passwords exported to passwords.txt")

def main():
    passwords = []
    print("Menu:")
    print("1. Generate a Random Password")
    print("2. Generate a Password Based on a Pattern")
    print("3. Generate a Password Using Personal Information")

    while True:
        choice = int(input("Enter your choice: "))
    
        if choice == 1:
            print("Generating a Random Password...")
            length = input("Enter the length of the password (press Enter for default length): ")
            length = int(length) if length else DEFAULT_LENGTH
            include_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
            include_numbers = input("Include numbers? (y/n): ").lower() == 'y'
            include_special_chars = input("Include special characters? (y/n): ").lower() == 'y'
            password = generate_password(length, include_uppercase, include_numbers, include_special_chars)
            passwords.append(password)
            print("Your password is:", password)
            pyperclip.copy(password)  # Copy the password to clipboard
            print("Password copied to clipboard.")
        elif choice == 2:
            print("Generating a Password Based on a Pattern...")
            pattern = input("Enter the password pattern (u for uppercase, l for lowercase, d for digit, s for special character, and any other character as is): ")
            password = generate_password_with_pattern(pattern)
            passwords.append(password)
            print("Your password is:", password)
            pyperclip.copy(password)  # Copy the password to clipboard
            print("Password copied to clipboard.")
        elif choice == 3:
            print("Generating a Password Using Personal Information...")
            name = input("Enter your name: ")
            birthdate = input("Enter your birthdate (MMDDYYYY): ")
            password = generate_password_with_personal_info(name, birthdate)
            passwords.append(password)
            print("Your password is:", password)
            pyperclip.copy(password)  # Copy the password to clipboard
            print("Password copied to clipboard.")
        else:
            print("Invalid choice. Please try again.")
            
        repeat = input("Do you want to generate another password? (y/n): ")
        if repeat.lower() != 'y':
            break

    export = input("Do you want to export the generated passwords to a file? (y/n): ")
    if export.lower() == 'y':
        export_passwords(passwords)

if __name__ == "__main__":
    main()