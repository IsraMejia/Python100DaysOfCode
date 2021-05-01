import D8art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def cesar(start_text, shift_amount, cipher_direction):
    end_text = ''
    if cipher_direction == 'decode':
        shift_amount *= -1 #To increment or decrement the alphabet index ;)

    for char in start_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_index = position + shift_amount
            end_text += alphabet[new_index]
        else:
            end_text += char #add the number, space or symbols
    
    print(f'\n\tThe {cipher_direction}d text is {end_text} \n')


print(D8art.logo)
# print(f'The lengt of the Alphabet  is {len(alphabet)} \n')
again  = 'yes'
while True :
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 27 

    cesar(start_text = text, shift_amount = shift, cipher_direction = direction)
    
    again = input('Do you want to restart the cipher program? \n[yes] / [no]\t :  ')
    if (again != 'yes'):
        print('\t\tgood bye :)\n') 
        break