import os
from cryptography.fernet import Fernet
from tabulate import tabulate

# Display welcome message to user.
def greet_user():
    print("=" * 60)
    print("Welcome to the Secure Password Manager!")
    print("Easily store and view your encrypted password securely.")
    print("=" * 60)

class PasswordManager:
    def __init__(self):
        self.key_file = "key.key"
        self.password_file = "password.txt"
        self.fernet = None
        self.initialize_key()

    # Ensure the key encryption key exist or generate new one.
    def initialize_key(self):
        if not os.path.exists(self.key_file):
            self.write_key()
            print("New encryption key generated and saved.")
        self.load_key()

    # Generate and save a new encryption key.
    def write_key(self):
        key = Fernet.generate_key()
        with open(self.key_file, "wb") as file:
            file.write(key)

    # Load the encryption key from the file.
    def load_key(self):
        with open(self.key_file, "rb") as file:
            key = file.read()
        self.fernet = Fernet(key)

    # Display stored account names and decrypted password in a table.
    def view_password(self):
        if not os.path.exists(self.password_file):
            print("No password saved yet. Add some passwords first.")
            return

        with open(self.password_file, "r") as file:
            data = [line.strip().split("|") for line in file.readlines()]

        if not data:
            print("No password saved yet. Add some passwords first.")
            return

        table_data = [[item[0], self.fernet.decrypt(item[1].encode()).decode()] for item in data]
        print("\n" + tabulate(table_data, headers=["Username", "Password"], tablefmt="grid") + "\n")

    # Add new username and its password.
    def add_password(self):
        username = input("Enter username: ").strip()
        password = input("Enter password: ").strip()

        if not username or not password:
            print("Please enter a username and a password.")
            return

        encrypted_password = self.fernet.encrypt(password.encode()).decode()
        with open(self.password_file, "a") as file:
            file.write(f"{username}|{encrypted_password}\n")

        print(f"Password for account '{username}' has been saved securely.")

    # Main program loop
    def run(self):
        greet_user()
        while True:
            print("\nOptions: [view] View passwords | [add] Add passwords | [q] Quit")
            mode = input("Select an option: ").strip().lower()

            if mode == "q":
                print("\nThank you for using the Secure Password Manager. Goodbye!")
                break
            elif mode == "view":
                self.view_password()
            elif mode == "add":
                self.add_password()
            else:
                print("Invalid option. Please try again.")

if __name__ == "__main__":
    manager = PasswordManager()
    manager.run()
