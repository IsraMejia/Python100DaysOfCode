print("Welcome to the tip calculator")
total = float(input("What was the total bill ?  $"))
porcent = float(input("What percentage tip would like to give? 10, 12 or 15? "))
npeople = int(input("How many people to split the bill? "))

eachPay = ( total +(total * (porcent/100 )) ) / npeople

print(f'\nEach person should pay: $ {round(eachPay, 2)}')

