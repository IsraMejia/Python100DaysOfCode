import math

print("\nThis program calculate how many cans you will have to buy, to paint a wall.")

test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5

def paint_calc( height, width , cover ):
    cans = math.ceil( (height * width) / cover) #math.ceil round the number to up   1.2 -> 2
    print(f'to print yout wall, you will have to buy: {cans}  cans :) ')


paint_calc(height=test_h, width=test_w, cover=coverage)
