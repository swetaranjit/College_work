# Playfair Cipher Program

def create_key_square(keyword):
    keyword = "".join(dict.fromkeys(keyword.upper().replace("J", "I")))  # Remove duplicates, replace J with I
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"  # I/J combined
    key_square = []

    for char in keyword:
        if char not in key_square and char in alphabet:
            key_square.append(char)

    for char in alphabet:
        if char not in key_square:
            key_square.append(char)

    # Create 5x5 grid
    grid = [key_square[i:i+5] for i in range(0, 25, 5)]
    return grid

def preprocess_text(text):
    text = text.upper().replace("J", "I").replace(" ", "")
    result = ""
    i = 0
    while i < len(text):
        a = text[i]
        b = ""
        if i+1 < len(text):
            b = text[i+1]
            if a == b:
                b = "X"
                i += 1
            else:
                i += 2
        else:
            b = "X"
            i += 1
        result += a + b
    return result

def find_position(grid, char):
    for row in range(5):
        for col in range(5):
            if grid[row][col] == char:
                return row, col

def playfair_encrypt(text, grid):
    cipher = ""
    for i in range(0, len(text), 2):
        a, b = text[i], text[i+1]
        row1, col1 = find_position(grid, a)
        row2, col2 = find_position(grid, b)
        if row1 == row2:
            cipher += grid[row1][(col1 + 1) % 5] + grid[row2][(col2 + 1) % 5]
        elif col1 == col2:
            cipher += grid[(row1 + 1) % 5][col1] + grid[(row2 + 1) % 5][col2]
        else:
            cipher += grid[row1][col2] + grid[row2][col1]
    return cipher

def playfair_decrypt(cipher, grid):
    text = ""
    for i in range(0, len(cipher), 2):
        a, b = cipher[i], cipher[i+1]
        row1, col1 = find_position(grid, a)
        row2, col2 = find_position(grid, b)
        if row1 == row2:
            text += grid[row1][(col1 - 1) % 5] + grid[row2][(col2 - 1) % 5]
        elif col1 == col2:
            text += grid[(row1 - 1) % 5][col1] + grid[(row2 - 1) % 5][col2]
        else:
            text += grid[row1][col2] + grid[row2][col1]
    return text

# --- Main Program ---
keyword = input("Enter keyword: ")
plaintext = input("Enter plaintext: ")

grid = create_key_square(keyword)
processed_text = preprocess_text(plaintext)
ciphertext = playfair_encrypt(processed_text, grid)
decrypted_text = playfair_decrypt(ciphertext, grid)

print("Key Square:")
for row in grid:
    print(row)
print("Processed Text:", processed_text)
print("Encrypted Text:", ciphertext)
print("Decrypted Text:", decrypted_text)