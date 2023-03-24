alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

if direction == "encode":
    encrypted_text = ""
    for char in text:
        if char in alphabet:
            char_index = alphabet.index(char)
            shifted_index = (char_index + shift) % 26
            encrypted_text += alphabet[shifted_index]
        else:
            encrypted_text += char
    print(f"The encrypted message is: {encrypted_text}")
elif direction == "decode":
    decrypted_text = ""
    for char in text:
        if char in alphabet:
            char_index = alphabet.index(char)
            shifted_index = (char_index - shift) % 26
            decrypted_text += alphabet[shifted_index]
        else:
            decrypted_text += char
    print(f"The decrypted message is: {decrypted_text}")
else:
    print("Invalid input. Please try again.")