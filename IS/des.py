from Crypto.Cipher import DES
from Crypto.Random import get_random_bytes
import base64

# DES requires 8-byte key
key = get_random_bytes(8)

# Padding function (DES block size = 8)
def pad(text):
    while len(text) % 8 != 0:
        text += ' '
    return text

# Create DES cipher
cipher = DES.new(key, DES.MODE_ECB)

# Input message
message = input("Enter message: ")
padded_message = pad(message)

# Encrypt
ciphertext = cipher.encrypt(padded_message.encode())
encoded_cipher = base64.b64encode(ciphertext).decode()

print("Encrypted message:", encoded_cipher)

# Decrypt
decipher = DES.new(key, DES.MODE_ECB)
decrypted = decipher.decrypt(ciphertext).decode().strip()

print("Decrypted message:", decrypted)