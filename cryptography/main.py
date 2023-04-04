# Darius Corbin
# 03/27/2023
# Vigenere Cipher

#   To encrypt a message using the Vigenère cipher, a keyword is chosen and repeated to match the length of the message.
#   Each letter of the message is then shifted by a number of positions equal to the numerical value of the corresponding
#   letter in the keyword, which is repeated as necessary.
#   For example, if the keyword is "LEMON" and the message is "ATTACKATDAWN", the first letter of the message would be
#   shifted by the numerical value of "L", which is 11, the second letter of the message would be shifted by
#   the numerical value of "E", which is 4, and so on.

#   To decrypt a message that has been encrypted using the Vigenère cipher, the keyword is used in reverse to shift
#   each letter of the message back to its original position. The numerical value of each letter in the keyword is
#   subtracted from the corresponding letter in the message to recover the original message.

#   Try message = "Good Morning" --> Key= Key

import string

def vigenere_cipher(message, key, mode):
    """
    Encrypt or decrypt the given message using the Vigenere cipher.

    Parameters:
    message (str): The message to encrypt/decrypt.
    key (str): The encryption key.
    mode (str): Either 'encrypt' or 'decrypt'.

    Returns:
    The encrypted or decrypted message.
    """
    # Create a lookup table of letter to number.
    alphabet = string.ascii_lowercase
    lookup_table = {letter: i for i, letter in enumerate(alphabet)}

    # Convert the key to lowercase.
    key = key.lower()

    # Create the key sequence by repeating the key.
    key_sequence = ''
    for i in range(len(message)):
        key_sequence += key[i % len(key)]

    # Encrypt or decrypt the message.
    result = ''
    for i, letter in enumerate(message):
        if letter.lower() not in alphabet:
            # Ignore non-letter characters.
            result += letter
            continue

        # Get the number value of the letter and key.
        letter_value = lookup_table[letter.lower()]
        key_value = lookup_table[key_sequence[i]]

        # Apply the encryption/decryption formula.
        if mode == 'encrypt':
            result_value = (letter_value + key_value) % 26
        elif mode == 'decrypt':
            result_value = (letter_value - key_value) % 26

        # Convert the result back to a letter and append to the result.
        result_letter = alphabet[result_value]
        if letter.isupper():
            result_letter = result_letter.upper()

        result += result_letter

    return result

# Example usage:
message = input("Enter a message: ")
key = input("Enter a key: ")
mode = input("Encrypt or decrypt? ").lower()

if mode == 'encrypt':
    encrypted = vigenere_cipher(message, key, 'encrypt')
    print(f"Encrypted message: {encrypted}")
elif mode == 'decrypt':
    decrypted = vigenere_cipher(message, key, 'decrypt')
    print(f"Decrypted message: {decrypted}")
else:
    print("Invalid mode. Please enter 'encrypt' or 'decrypt'.")
