# print(f'module 3 of 39 = {39%3}')#Taths right, children play jaja
print('Now i will hack the Fizzbuzz B) jaja')

for number in range (1, 101, 1):
    if( ((number%3) == 0) and ((number%5) == 0) ):
        print('FizzBuzz')
    elif( (number%3) == 0):
        print('Fizz')
    
    elif ( (number%5) == 0):
        print('Buzz')
    
    else:
        print(number)