print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

side = input('Do you wanna got to left or right?').lower()
if (side == 'left'):
    action = input('Now, you come to a Lake. There is in an island in the middle of the lake.\nAre you going to "wait" for a boat or do you prefer to "swim"?').lower()
    
    if(action == 'swim'):
        print('Attacked by trout, game over')
    
    else:
        print('You arrive at the island unharmed. There is a house with 3 doors. One "red", one "yellow" and one "blue" ')
        door = input('Which colour dou you choose?').lower()

        if door == 'red':
            print('Burned by fire, GameOver ')
        elif door == 'yellow':
            print('You win B) ')
        elif door == 'blue':
            print('Eaten by beasts, GameOver')
        else :print('You dead bro jaja')       
        
else:
    print('Fall into a hole. Game over')

