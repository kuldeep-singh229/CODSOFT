import random
import string

def generate_password(length):
    # Define possible characters (letters, digits, punctuation)
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Randomly choose characters
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    try:
        length = int(input("Enter the desired password length: "))
        if length < 4:
            print("Password length should be at least 4 characters for better security.")
        else:
            password = generate_password(length)
            print(f"\nGenerated Password: {password}")
    except ValueError:
        print("Please enter a valid number!")

if __name__ == "__main__":
    main()

