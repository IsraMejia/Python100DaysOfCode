import D10_artCalculator
import os #to clear the terminal        os.system('cls' if os.name == 'nt' else 'clear')  

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

operations = {
    """We can use the dictionaries like switch case , AWSOMEEEE """
    '+' : add,
    '-' : subtract,
    '*' : multiply,
    '/' : divide,
}


num1 = int(input("What's is the first number?  "))
num2 = int(input("What's is the second number?  "))

for symbol in operations: 
    print(symbol)

operation_symbol = input("Picl an operation from the line above: ")

calculation_function = operations[operation_symbol] #select the function (Like switch case)
result = calculation_function(num1, num2) #Pass the number to the selecterd function 👀

print(f"\t\t{num1} {operation_symbol} {num2} = {result}")