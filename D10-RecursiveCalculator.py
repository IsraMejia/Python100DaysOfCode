import os #to clear the terminal  
from D10_artCalculator import logo

def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}

def calculator():
  print(logo)

  num1 = float(input("What's the first number?: "))
  for symbol in operations:
    print(symbol)
  should_continue = True
 
  while should_continue:
    operation_symbol = input("Pick an operation: ")
    num2 = float(input("What's the next number?: "))
    calculation_function = operations[operation_symbol]
    answer = calculation_function(num1, num2)
    print(f"{num1} {operation_symbol} {num2} = {answer}")
    
    again = input(f'Dou you want continue calculation with {answer} ? [yes] / [no] \n or [new] to restart a new calculator \t\t\t:   ').lower() 
    if again == 'yes':
      num1 = answer
    elif again == 'new':
      should_continue = False
      os.system('cls' if os.name == 'nt' else 'clear')  
      calculator() # <------ recursion
    elif again == 'no':
      print('\t\t\t Bye :)\n')
      should_continue =False
    else:
      print('\t\t\t Invalid input \n')

calculator()