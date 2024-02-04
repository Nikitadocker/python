from check_prime_module import check_prime
from check_input_module import check_input


input_is_good = False
while input_is_good == False:
    start_number = int(input())
    finish_number = int(input())
    input_is_good = check_input(start_number,finish_number)
   
    
    
check_prime(start_number, finish_number)