
import os

def welcome():
    """Prints a welcome message."""
    print("Welcome to the Caesar Cipher")
    print("This program encrypts and decrypts text using the Caesar Cipher.")

def enter_message():
    """Prompts the user to choose a mode and enter a message."""
    while True:
        mode = input("Would you like to encrypt (e) or decrypt (d): ").lower()
        if mode in ['e', 'd']:
            break
        print("Invalid Mode")

    while True:
        try:
            shift = int(input("What is the shift number (0-25): "))
            if 0 <= shift <= 25:
                break
            print("Shift must be between 0 and 25")
        except ValueError:
            print("Invalid Shift")

    return mode, shift

def encrypt(message, shift):
    """Encrypts a message using the Caesar Cipher."""
    result = []
    for char in message:
        if char.isalpha():
            result.append(chr((ord(char) - 65 + shift) % 26 + 65))
        else:
            result.append(char)
    return ''.join(result)

def decrypt(message, shift):
    """Decrypts a message using the Caesar Cipher."""
    result = []
    for char in message:
        if char.isalpha():
            result.append(chr((ord(char) - 65 - shift) % 26 + 65))
        else:
            result.append(char)
    return ''.join(result)

def is_file(filename):
    """Checks if a file exists in the current directory."""
    return os.path.isfile(filename)

def process_file(filename, mode, shift):
    """Processes a file to encrypt or decrypt its content."""
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
        if mode == 'e':
            return [encrypt(line.strip().upper(), shift) for line in lines]
        else:
            return [decrypt(line.strip().upper(), shift) for line in lines]
    except FileNotFoundError:
        print("File not found!")
        return []

def write_messages(messages):
    """Writes messages to a file named results.txt."""
    with open('results.txt', 'w') as file:
        for message in messages:
            file.write(message + '\n')
    print("Output written to results.txt")

def message_or_file():
    """Prompts the user to choose between console input or file input."""
    while True:
        mode = input("Would you like to encrypt (e) or decrypt (d): ").lower()
        if mode in ['e', 'd']:
            break
        print("Invalid Mode")

    while True:
        source = input("Would you like to read from a file (f) or the console (c)? ").lower()
        if source in ['f', 'c']:
            break
        print("Invalid choice")

    if source == 'f':
        while True:
            filename = input("Enter a filename: ")
            if is_file(filename):
                break
            print("Invalid Filename")

        while True:
            try:
                shift = int(input("What is the shift number (0-25): "))
                if 0 <= shift <= 25:
                    break
                print("Shift must be between 0 and 25")
            except ValueError:
                print("Invalid Shift")

        return mode, None, filename, shift

    while True:
        try:
            shift = int(input("What is the shift number (0-25): "))
            if 0 <= shift <= 25:
                break
            print("Shift must be between 0 and 25")
        except ValueError:
            print("Invalid Shift")

    return mode, None, None, shift

def main():
    """Main function to run the Caesar Cipher program."""
    welcome()
    while True:
        mode, message, filename, shift = message_or_file()

        if filename:
            processed_lines = process_file(filename, mode, shift)
            if processed_lines:
                write_messages(processed_lines)
        else:
            message = input(f"What message would you like to {'encrypt' if mode == 'e' else 'decrypt'}: ").upper()
            if mode == 'e':
                print("Encrypted Message:", encrypt(message, shift))
            else:
                print("Decrypted Message:", decrypt(message, shift))

        again = input("Would you like to encrypt or decrypt another message? (y/n): ").lower()
        if again == 'n':
            print("Thanks for using the program, goodbye!!")
            break

main()
