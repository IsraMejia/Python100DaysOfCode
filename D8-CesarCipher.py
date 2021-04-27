alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encrypt(plain_text, shift_amount):
    cipher_text = ''
    for c in plain_text :
        index = alphabet.index(c) #Return the index of the match between the caracter 'c' with its identical element in the list
        new_index = index + shift_amount
        # new_index = (new_index > 30 ) ? new_index -= 30 : new_index ;
        new_letter = alphabet[new_index]
        cipher_text += new_letter
    
    print(f'The encoded text is {cipher_text}')

def dencrypt(plain_text, shift_amount):
    cipher_text = ''
    for c in plain_text :
        index = alphabet.index(c) #Return the index of the match between the caracter 'c' with its identical element in the list
        new_index = index - shift_amount
        # new_index = (new_index > 30 ) ? new_index -= 30 : new_index ;
        new_letter = alphabet[new_index]
        cipher_text += new_letter
    
    print(f'The encoded text is {cipher_text}')


direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")

text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

if direction == 'encode':
    encrypt(plain_text = text, shift_amount = shift)
elif direction == 'decode':
    dencrypt(plain_text = text, shift_amount = shift)
else:
    print('Invalid Direction') 