def caesar_cipher(text, key):
    result = ""

    for char in text:
        if char.isalpha():  # Check if character is a letter
            shift_base = 65 if char.isupper() else 97
            result += chr((ord(char) - shift_base + key) % 26 + shift_base)
        else:
            result += char  # Keep spaces and symbols unchanged

    return result


# User input
text = input("Enter text: ")
key = int(input("Enter key value: "))

# Encryption
encrypted = caesar_cipher(text, key)
print("Encrypted text:", encrypted)

# Decryption
decrypted = caesar_cipher(encrypted, -key)
print("Decrypted text:", decrypted)