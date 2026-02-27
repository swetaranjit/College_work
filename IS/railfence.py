# Simple Rail Fence Cipher

def encrypt_rail_fence(text, rails):
    fence = [""] * rails
    rail, step = 0, 1

    for char in text:
        fence[rail] += char
        rail += step
        if rail == 0 or rail == rails - 1:
            step *= -1

    return "".join(fence)

def decrypt_rail_fence(cipher, rails):
    # Create pattern
    pattern = [0] * len(cipher)
    rail, step = 0, 1
    for i in range(len(cipher)):
        pattern[i] = rail
        rail += step
        if rail == 0 or rail == rails - 1:
            step *= -1

    # Fill rails
    rails_list = [""] * rails
    index = 0
    for r in range(rails):
        for i in range(len(cipher)):
            if pattern[i] == r:
                rails_list[r] += cipher[index]
                index += 1

    # Read zigzag
    result = ""
    rail_pos = [0] * rails
    rail, step = 0, 1
    for i in range(len(cipher)):
        result += rails_list[rail][rail_pos[rail]]
        rail_pos[rail] += 1
        rail += step
        if rail == 0 or rail == rails - 1:
            step *= -1
    return result

# --- Main ---
text = input("Enter text: ")
rails = int(input("Enter number of rails: "))

cipher = encrypt_rail_fence(text, rails)
print("Encrypted:", cipher)
print("Decrypted:", decrypt_rail_fence(cipher, rails))