# vault.py

from cryptography.fernet import Fernet

# Load the encryption key from file
def load_key():
    return open("key.key", "rb").read()

# Encrypt the password
def encrypt_password(password, key):
    f = Fernet(key)
    return f.encrypt(password.encode())

# Decrypt the password
def decrypt_password(encrypted_password, key):
    f = Fernet(key)
    return f.decrypt(encrypted_password).decode()

# Add a new password
def add_password():
    site = input("Enter the site name: ")
    username = input("Enter the username: ")
    password = input("Enter the password: ")

    encrypted = encrypt_password(password, key)

    with open("passwords.txt", "a") as f:
        f.write(f"{site} | {username} | {encrypted.decode()}\n")

    print("Password saved successfully!")

# View stored passwords
def view_passwords():
    try:
        with open("passwords.txt", "r") as f:
            for line in f:
                site, username, encrypted = line.strip().split(" | ")
                decrypted = decrypt_password(encrypted.encode(), key)
                print(f"{site} | {username} | {decrypted}")
    except FileNotFoundError:
        print("No passwords stored yet.")

# Main Menu
key = load_key()

while True:
    print("\n--- Password Vault ---")
    choice = input("Choose: add / view / quit: ").lower()

    if choice == "add":
        add_password()
    elif choice == "view":
        view_passwords()
    elif choice == "quit":
        break
    else:
        print("Invalid option. Please choose again.")