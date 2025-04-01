import random
import string

def generate_password(length, use_uppercase, use_numbers, use_special_chars):
    # Define character pools
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase if use_uppercase else ""
    numbers = string.digits if use_numbers else ""
    special_chars = string.punctuation if use_special_chars else ""

    # Combine all selected character pools
    all_characters = lowercase_letters + uppercase_letters + numbers + special_chars

    if not all_characters:
        raise ValueError("No character types selected for password generation.")

    # Generate the password
    password = ''.join(random.choices(all_characters, k=length))
    return password

def main():
    print("Welcome to the Password Generator!")

    # Get user preferences
    try:
        # Validate password length
        while True:
            try:
                length = int(input("Enter the desired password length: "))
                if length <= 0:
                    print("Password length must be a positive integer. Please try again.")
                else:
                    break
            except ValueError:
                print("Invalid input. Please enter a valid number.")

        # Validate character type preferences
        while True:
            use_uppercase = input("Include uppercase letters? (y/n): ").lower() == "y"
            use_numbers = input("Include numbers? (y/n): ").lower() == "y"
            use_special_chars = input("Include special characters? (y/n): ").lower() == "y"

            if use_uppercase or use_numbers or use_special_chars:
                break
            else:
                print("You must select at least one character type. Please try again.")

        # Generate the password
        password = generate_password(length, use_uppercase, use_numbers, use_special_chars)
        print(f"\nYour generated password is: {password}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()