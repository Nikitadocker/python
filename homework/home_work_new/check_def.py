def check_prime (number):
       prime = True
       for divider in range(2, number):
           if number % divider == 0:
               prime = False
               break
       if prime:
           return  True
       else:
           return False
