import secrets
import string

def generate_password(length):
    # Define the characters to use in the password
    characters = string.ascii_letters + string.digits + string.punctuation
    # Generate a random password
    password = ''.join(secrets.choice(characters) for _ in range(length))
    return password

# Main program
print("Password Generator")
length = int(input("Enter the desired length of the password: "))
password = generate_password(length)
print(f"Generated password: {password}")