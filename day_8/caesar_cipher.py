alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']



def ceasar(direction, text, shift):
    new_text = ""
    if direction == "decode":
        shift *= -1
    for char in text:
        if char not in alphabet:
            new_text += char
        else:
            position = alphabet.index(char) + shift
            new_text += alphabet[position]
    return new_text

while True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26
    print(ceasar(direction, text, shift))

    if input("do you want to continue? yes|no").lower() == "no":
        break

