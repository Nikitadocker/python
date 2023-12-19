# start_range = int(input())

# finish_range = int(input())

# for number_for_check in range(start_range, finish_range + 1):
#     prime = True
#     for divisor in range (2, number_for_check):
#         if number_for_check % divisor == 0:
#             prime = False
#             break
#     if prime:
#         print ("Число {} простым ".format(number_for_check))
#     else:
#         print ("Число {} cоставное ".format(number_for_check))

import sys

start_range = int(input())

finish_range = int(input())

if start_range < 0 or finish_range < 0:
    sys.exit("Числа для проверки должны быть больше 0")
else: 
    start_range = int(start_range)  
    finish_range = int (finish_range)

number_for_check = start_range

while number_for_check < finish_range:
    prime = True
    divisor = 2
    while divisor < number_for_check:
        if number_for_check % divisor == 0:
            prime = False
            break
        divisor += 1
    if prime:
        print ("Число {} простым ".format(number_for_check))
    else:
        print ("Число {} cоставное ".format(number_for_check))
    number_for_check += 1
    