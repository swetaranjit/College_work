# Simple RSA implementation

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def mod_inverse(e, phi):
    for d in range(1, phi):
        if (d * e) % phi == 1:
            return d

# Step 1: choose primes
p = 3
q = 11

# Step 2: compute n and phi
n = p * q
phi = (p - 1) * (q - 1)

# Step 3: choose e
e = 3
while gcd(e, phi) != 1:
    e += 1

# Step 4: find d
d = mod_inverse(e, phi)

print("Public Key:", (e, n))
print("Private Key:", (d, n))

# Input message (number form)
msg = int(input("Enter message (number < n): "))

# Encryption
cipher = (msg ** e) % n
print("Encrypted message:", cipher)

# Decryption
decrypted = (cipher ** d) % n
print("Decrypted message:", decrypted)