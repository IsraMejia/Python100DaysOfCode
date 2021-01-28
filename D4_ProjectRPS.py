import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# print(rock)
def print_choice(choice):
    if(choice == 1):
        print(rock)
    elif(choice == 2):
        print(paper)
    elif(choice == 3):
        print(scissors)
    else: 
        print('Impossible, GameOver')

 


while True:
    print('\n\nAre u ready for play Rock, Paper, Scissors with a computer xd?')

    choice = int(input('What do you choice? Type 1 for Rock, 2 for Paper or 3 for Scissors'))
    computer_choice = random.randint(1, 3)

    print_choice(choice)
    print('My computer choice is:')
    print_choice(computer_choice)    

    if  choice >= 4 or  choice < 1: 
        print("You typed an invalid number, you lose!") 
    elif  choice == 1 and computer_choice == 3:
        print("You win!")
    elif computer_choice == 1 and  choice == 3:
        print("You lose")
    elif computer_choice >  choice:
        print("You lose")
    elif  choice > computer_choice:
        print("You win!")
    elif computer_choice ==  choice:
        print("It's a draw")

    choise_play = input('Dou you wanna play again? ').lower()
    # print(f'choise : {choise_play}')    
    if (choise_play == 'no'):
        break




# python3 D4_ProjectRPS.py