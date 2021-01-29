print('Are u ready to see my magic?')
print('Here is the sum of all even numbres from 1 to 100')

even_sum = 0
for even_number in range( 2, 101, 2):
    even_sum += even_number

print(f'The result is: {even_sum}')