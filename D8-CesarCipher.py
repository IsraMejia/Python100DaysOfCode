alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def cesar(start_text, shift_amount, cipher_direction):
    end_text = ''
    if cipher_direction == 'decode':
        shift_amount *= -1 #To increment or decrement the alphabet index ;)
        
    for new_letter in start_text:
        position = alphabet.index(new_letter)
        new_index = position + shift_amount
        end_text += alphabet[new_index]
    
    print(f'The {cipher_direction}d text is {end_text}')



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

# if direction == 'encode':
#     encrypt(plain_text = text, shift_amount = shift)
# elif direction == 'decode':
#     dencrypt(plain_text = text, shift_amount = shift)
# else:
#     print('Invalid Direction') 
cesar(start_text = text, shift_amount = shift, cipher_direction = direction)