import sys

def check_range_numbers(start_number, finish_number):
    if start_number < 0 or finish_number < 0:
        return sys.exit ('В диапозон могут входить только числа больше нуля')
    if start_number > 0 and finish_number > 0:
        for number_for_check in range(start_number, finish_number + 1):
            prime = True
            print (number_for_check)
            for divider in range(2, number_for_check):
                print (divider)
                if number_for_check % divider == 0:
                    prime = False
                    break
            if prime:
                return print('Число {} простое'.format(number_for_check))
            else:
                return print('Число {} cocтавное'.format(number_for_check))
    
start_number = int(input())
finish_number = int(input())

check_range_numbers(start_number, finish_number)


# import sys

# def check_range_numbers(start_number, finish_number):
#     if start_number < 0 or finish_number < 0:
#         sys.exit('В диапазон могут входить только числа больше нуля')

#     if start_number > 0 and finish_number > 0:
#         for number_for_check in range(start_number, finish_number + 1):
#             prime = True
#             print(number_for_check)
#             for divider in range(2, number_for_check):
#                 print(divider)
#                 if number_for_check % divider == 0:
#                     prime = False
#                     break  # используем break вместо return
#             if prime:
#                 print('Число {} простое'.format(number_for_check))
#             else:
#                 print('Число {} составное'.format(number_for_check))

# start_number = int(input())
# finish_number = int(input())

# check_range_numbers(start_number, finish_number)
