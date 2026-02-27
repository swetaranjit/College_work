# Vigenere Cipher (Repeating Key Version)

text = input("Enter plaintext: ")
key = input("Enter key: ")

# Function to repeat key
def generate_key(text, key):
    extended_key = ""
    key_index = 0
    
    for char in text:
        if char.isalpha():
            extended_key += key[key_index % len(key)]
            key_index += 1
        else:
            extended_key += char
    return extended_key

extended_key = generate_key(text, key)

# Encryption
cipher = ""
for i in range(len(text)):
    if text[i].isalpha():
        shift_base = 65 if text[i].isupper() else 97
        
        p = ord(text[i]) - shift_base
        k = ord(extended_key[i].lower()) - 97
        
        c = (p + k) % 26
        cipher += chr(c + shift_base)
    else:
        cipher += text[i]

print("Encrypted text:", cipher)

# Decryption
decrypted = ""
for i in range(len(cipher)):
    if cipher[i].isalpha():
        shift_base = 65 if cipher[i].isupper() else 97
        
        c = ord(cipher[i]) - shift_base
        k = ord(extended_key[i].lower()) - 97
        
        p = (c - k) % 26
        decrypted += chr(p + shift_base)
    else:
        decrypted += cipher[i]

print("Decrypted text:", decrypted)