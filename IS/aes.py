from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import base64

# Function to pad message (AES requires multiples of 16 bytes)
def pad(text):
    while len(text) % 16 != 0:
        text += ' '
    return text

# Generate a random 16-byte key
key = get_random_bytes(16)

# Create AES cipher
cipher = AES.new(key, AES.MODE_ECB)

# Input message
message = input("Enter message: ")
padded_message = pad(message)

# Encrypt
ciphertext = cipher.encrypt(padded_message.encode())

# Encode for display
encoded_cipher = base64.b64encode(ciphertext).decode()
print("Encrypted message:", encoded_cipher)

# Decrypt
decipher = AES.new(key, AES.MODE_ECB)
decrypted = decipher.decrypt(ciphertext).decode().strip()

print("Decrypted message:", decrypted)