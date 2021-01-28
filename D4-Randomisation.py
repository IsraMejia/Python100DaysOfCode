import random
import D4_my_module

random_interger = random.randint(1, 10) #Betwen 1 and 10
print(f'\nThe random number is: {random_interger}')
print(f'\n Pi = {D4_my_module.pi}' )

random_float = random.random() #Return a value between [0.0 , 1)
print(f'\nMy  random float is: {random_float}')

random_interger2 = random.randint(0, 5) #Betwen 0 and 5
print(f'\nThe random number is: {random_interger2}')

random_float *= 5 #Betwen 0 and 5 with float
print(f'\nMy  random float  now is: {random_float}')

love_score = random.randint(1, 100)
print(f'\n Your love score is : {love_score}')