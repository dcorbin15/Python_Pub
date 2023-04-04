# Darius Corbin
# 03/20/2023
# Affine Cipher

#    For encryption: The numerical value of each letter is then transformed using the formula (ax + b) % 26,
#    where x is the numerical value of the letter, a is the encryption key, b is the modular arithmetic key,
#    and % 26 is used to keep the result within the range of the alphabet.
#    If a=5 and b=8, then the letter 'A' (which has a numerical value of 0) would be transformed into the letter 'I'
#    (which has a numerical value of 8), using the formula (5*0 + 8) % 26 = 8.
#    If encrypt is chose try value a: 5 and value b: 8

#   For decryption: the formula (a^-1(y - b)) % 26 is used, where y is the numerical value of the ciphertext letter,
#   a^-1 is the modular multiplicative inverse of the encryption key modulo 26, and b is the modular arithmetic key.
#   The modular multiplicative inverse of a is a number x such that (a * x) % 26 = 1.



def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

def mod_inverse(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

def affine_encrypt(message, a, b):
    ciphertext = ''
    for char in message:
        if char.isalpha():
            # Apply the affine cipher transformation
            char_value = ord(char.upper()) - 65
            cipher_value = ((a * char_value) + b) % 26
            ciphertext += chr(cipher_value + 65)
        else:
            ciphertext += char
    return ciphertext

def affine_decrypt(ciphertext, a, b):
    message = ''
    # Calculate the modular inverse of a
    a_inv = mod_inverse(a, 26)
    if a_inv is None:
        return None
    else:
        for char in ciphertext:
            if char.isalpha():
                # Apply the affine cipher transformation
                char_value = ord(char.upper()) - 65
                plain_value = ((char_value - b) * a_inv) % 26
                message += chr(plain_value + 65)
            else:
                message += char
        return message

# Ask the user whether they want to encrypt or decrypt
while True:
    mode = input("Would you like to encrypt or decrypt? ").lower()
    if mode not in ['encrypt', 'decrypt']:
        print("Invalid choice. Please try again.")
    else:
        break

# Ask the user for the message and key
message = input("Enter your message: ")
a = int(input("Enter the value for a: "))
b = int(input("Enter the value for b: "))

# Check that a and b are relatively prime
if gcd(a, 26) != 1:
    print("Error: a and 26 are not relatively prime.")
else:
    # Encrypt or decrypt the message
    if mode == 'encrypt':
        ciphertext = affine_encrypt(message, a, b)
        print(f"Ciphertext: {ciphertext}")
    else:
        plaintext = affine_decrypt(message, a, b)
        if plaintext is None:
            print("Error: a and 26 are not relatively prime.")
        else:
            print(f"Plaintext: {plaintext}")
