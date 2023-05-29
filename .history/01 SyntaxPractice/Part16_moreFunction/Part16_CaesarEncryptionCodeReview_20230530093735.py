alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def ceasar(start_text, shift_amout, cipher_directiion):
    display = ''
    for i in start_text:
        position = alphabet.index(i)
        if cipher_directiion == "decode":
           shift_amout = shift_amout * -1
        new_position = position + shift_amout
        display += alphabet[new_position]
    print(f"The {cipher_directiion}d text is {display} ")

ceasar(start_text=text, shift_amout=shift, cipher_directiion=direction)