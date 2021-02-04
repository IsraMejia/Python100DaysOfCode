import random
import D7_hangman_words as hmw
import D7_hangman_art as hma

# word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(hmw.word_list) #Take a random intem of the list 
word_len = len(chosen_word)
display = []
win = False
lives = 6
 
print(hma.logo)

for letter in chosen_word:
    display.append("_")
print(display)

print(f'\nThe magic word is: {chosen_word} \n')

while not win :
    
    guess =  input("\n\nGuess a letter: ").lower()

    if guess in display : 
        print(f"You've already guessed {guess}")
    
    for i in range(word_len) : 
        if  chosen_word[i] == guess : 
            display[i] = chosen_word[i]  
    
    if guess not in chosen_word:
        lives -= 1
        print(f"Error, {guess} is not in the word\n now you have {lives} lives\n")
        if lives == 0 : 
            win = True #No win the play xd, but, we need to stop the game jaja
            print("\n\t\t You lose jaja")

    print(display)

    print(hma.stages[lives] )

    if "_" not in display :
        win = True
        print('\n\tYou win broo, good done B) \n')
