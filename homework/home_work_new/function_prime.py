import sys
def check_prime (number):
    if number < 0:
       return sys.exit('Число должно быть положительным!')
    if number > 1:
       prime = True
       for divider in range(2, number):
           if number % divider == 0:
               prime = False
               break
       if prime:
           return print ('Число является простым')
       else:
           return print ('Число является составным')
       

number = int(input())

check_prime(number)