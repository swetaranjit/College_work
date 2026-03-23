# Diffie-Hellman Key Exchange

# Public values
p = 23   # prime number
g = 5    # primitive root

# Private keys (chosen secretly)
a = int(input("Enter private key of User A: "))
b = int(input("Enter private key of User B: "))

# Compute public keys
A = (g ** a) % p
B = (g ** b) % p

print("Public value of A:", A)
print("Public value of B:", B)

# Compute shared secret key
key_A = (B ** a) % p
key_B = (A ** b) % p

print("Secret key computed by A:", key_A)
print("Secret key computed by B:", key_B)