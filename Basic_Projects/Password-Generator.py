import random
import string

print("Hi, Welcome to drowssaP rotareneG ")
DEFAULT_LENGTH = 12

def generate_password(length=DEFAULT_LENGTH, use_uppercase=False, use_numbers=False, use_special_chars=False):
    chars = string.ascii_lowercase
    if use_uppercase:
        chars += string.ascii_uppercase
    if use_numbers:
        chars += string.digits
    if use_special_chars:
        chars += string.punctuation

    password = ''.join(random.choice(chars) for _ in range(length))
    return password

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

def generate_password_with_personal_info(name, birthdate):
    password = name[:3] + birthdate[-4:]
    return password

def main():
    print("1. Generate a Password")
    print("2. Generate a Password with Pattern")
    print("3. Generate a Password with Personal Info")

    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        print("Vaathiyarey please lock option 1, Click enter to continue")
        input()
        length = input("Enter the length of the password (press Enter for default length): ")
        length = int(length) if length else DEFAULT_LENGTH
        use_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
        use_numbers = input("Include numbers? (y/n): ").lower() == 'y'
        use_special_chars = input("Include special characters? (y/n): ").lower() == 'y'
        password = generate_password(length, use_uppercase, use_numbers, use_special_chars)
        print("Your password is:", password)
    elif choice == 2:
        print("Vaathiyarey please lock option 2, Click enter to continue")
        input()
        pattern = input("Enter the password pattern (u for uppercase, l for lowercase, d for digit, s for special character, and any other character as is): ")
        password = generate_password_with_pattern(pattern)
        print("Your password is:", password)
        
    elif choice == 3:
        print("Vaathiyarey please lock option 3, Click enter to continue")
        input()
        name = input("Enter your name: ")
        birthdate = input("Enter your birthdate (MMDDYYYY): ")
        password = generate_password_with_personal_info(name, birthdate)
        print("Your password is:", password)
    else:
        print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()