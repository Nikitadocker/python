import sys
from check_def import check_prime
from homework.function_for_check_prime.def_check_input import check_input

start_number, finish_number = check_input()

if start_number < 0 or finish_number < 0:
    sys.exit ("Числа для проверки должны быть положительными")

for number_for_check in range(start_number, finish_number + 1):
    if check_prime(number_for_check):
        print ("Число {} простое".format(number_for_check))
    else:
        print ("Число {} cоставное".format(number_for_check))