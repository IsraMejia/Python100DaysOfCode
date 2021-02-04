import random
#Step 1 
word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
chosen_word = random.choice(word_list) #Take a random intem of the list 
display = []
word_len = len(chosen_word)

for letter in chosen_word:
    display.append("_")
print(display)

print(f'\nThe magic word is: {chosen_word} \n')
#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
guess =  input("Guess a letter: ").lower()

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
for i in range(word_len) : 
    if  chosen_word[i] == guess :
        # print("Right")
        display[i] = chosen_word[i] 
        # print(f'letter = {letter}   and   guess = {guess} \n')
    # else:
        # print("Wrong")
        # print(f'letter = {letter}   and   guess = {guess} \n')

print(display)
