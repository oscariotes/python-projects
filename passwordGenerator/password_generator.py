# import string
# import secrets

# # Generate a random password

# alphabet = string.ascii_letters + string.digits
# special = string.punctuation + '!@#$%^&*()'
# password = ''.join(secrets.choice(alphabet + special ) for i in range(8))

# print(password)

import string
import secrets

def generate_password(length):
    alphabet = string.ascii_letters + string.digits
    special = string.punctuation + '!@#$%^&*()'
    password = ''.join(secrets.choice(alphabet + special) for i in range(length))
    return password

def main():
    while True:
        try:
            length = int(input("Enter the length of the password: "))
            if length < 5:
                print("Password length should be at least 6 characters.")
            else:
                password = generate_password(length)
                print("Generated Password:", password)
        except ValueError:
            print("Please enter a valid integer for the password length.")

if __name__ == "__main__":
    main()

