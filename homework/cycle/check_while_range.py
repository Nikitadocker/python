

number_for_check = 2
delitel = 2

while number_for_check <= 10:
    prime = True
    number_for_check += 1
    # print(number_for_check, prime)
    while delitel < number_for_check:
        if number_for_check % delitel == 0:
            prime = False
            print("Число {} составное".format(number_for_check))
            break
        delitel += 1

if prime == True:
        print("Число {} простоe".format(number_for_check))
