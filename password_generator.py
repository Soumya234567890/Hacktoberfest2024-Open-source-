import random
import string

class PasswordGenerator:
    def __init__(self, length):
        self.length = length

    def generate_password(self):
        all_characters = string.ascii_letters + string.digits + string.punctuation
        if self.length < 8:
            print("Password length should be at least 8 characters.")
            return None
        password = ''.join(random.choice(all_characters) for i in range(self.length))
        return password

# Create an instance of the PasswordGenerator class
password_generator = PasswordGenerator(12)

# Generate a password
password = password_generator.generate_password()

print(f"Generated password: {password}")
