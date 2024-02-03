import sys
from check_def import check_prime

start_number = int(input())
finish_number = int(input())

if start_number < 0 or finish_number < 0:
    sys.exit ("Числа не могут быть отрицательными")
elif start_number > finish_number:
    sys.exit ("Конец диапозона должен быть больше чем начало")
elif start_number == 0 or finish_number == 0:
    sys.exit ("0 не может быть простым числом")


check_prime (start_number, finish_number)