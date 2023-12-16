

# number_for_check = 2
# delitel = 2

# while number_for_check <= 10:
#     prime = True
#     delitel = 2
#     # print(number_for_check, prime)
#     while delitel < number_for_check:
#         if number_for_check % delitel == 0:
#             prime = False
#             print("Число {} составное".format(number_for_check))
#             break
#         delitel += 1

#     if prime == True:
#         print("Число {} простоe".format(number_for_check))



number_for_check = 2

while number_for_check <= 10:
    prime = True
    delitel = 2  
    print(number_for_check)
    while delitel < number_for_check:
        if number_for_check % delitel == 0:
            prime = False
            print("Число {} составное".format(number_for_check))
            break
        delitel += 1

    if prime:
        print("Число {} простое".format(number_for_check))

    number_for_check += 1
