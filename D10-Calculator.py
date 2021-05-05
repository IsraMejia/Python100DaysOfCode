import D10_artCalculator
import os #to clear the terminal        

print('\t\t Calculator program')
print(D10_artCalculator.logo)

def add(n1, n2): #Add
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2): 
    return n1 * n2

def divide(n1, n2): 
    return n1 / n2

operations = { #We can use the dictionaries like switch case , AWSOMEEEE 
    '+' : add, 
    '-' : subtract,
    '*' : multiply,
    '/' : divide,
}

calculate = True
again = 'new'
while calculate:
    if again == 'new':
        num1 = float(input("What's is the first number?  "))
    for symbol in operations: 
        print(symbol)
    operation_symbol = input("Pick an operation from the line above: ")
    num2 = float(input("What's is the second number?  "))

    calculation_function = operations[operation_symbol] #select the function (Like switch case)
    result = calculation_function(num1, num2) #Pass the number to the selecterd function 👀
    print(f"\t\t{num1} {operation_symbol} {num2} = {result}\n")
    num1 = result
    again = input(f'Dou you want continue calculation with {result} ? [yes] / [no] \n or [new] to restart a new calculator \t:   ').lower()
    if again == 'yes':
        calculate = True
    elif again == 'no':
        print('\t\t\t Bye :)\n')
        calculate = False
    elif again == 'new':
        os.system('cls' if os.name == 'nt' else 'clear') 
        print(f'\t\t Calculator program \n {D10_artCalculator.logo}') 
        print('Lets calculate')
    else:
        print('\t\tInvalid input\n')
        calculate = False

    
    

# operation_symbol = input("Pick another operation : ")
# num3 = int(input("What's is the second number?  "))
# calculation_function = operations[operation_symbol] #select the function (Like switch case)
# second_result = calculation_function(result, num2) #Pass the number to the selecterd function 👀
# print(f"\t\t{result} {operation_symbol} {num2} = {second_result}")