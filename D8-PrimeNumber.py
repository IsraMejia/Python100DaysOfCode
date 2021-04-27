print('This program shows you, if some number is prime or not 👀')

def prime_checker(number):
    is_prime = True
    for i in range(2, number):
        if  (number % i  == 0 ):    # 7/2 ,7/3, 7/$
            is_prime = False
        if is_prime == False :
            print('NOT a prime')
            break
            
    if is_prime == True:
        print('Is prime')


n = int(input("Check this number: "))
prime_checker(number=n)
