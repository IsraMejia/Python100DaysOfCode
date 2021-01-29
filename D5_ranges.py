for number in range(1, 10): #range goes from (1, 10] -> 1 to 9 with delta 1
    print(number)

print("\n 2 range, delta3:")
for number in range(1, 10, 3): #range goes from (1, 10] , delta 3
    print(number)

total = 0
print("\n 3  ")
for number in range(1, 100): #range goes from (1, 10] , delta 3
    total += number
print(total)