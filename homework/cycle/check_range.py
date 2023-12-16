range_for_check = range(2, 10)


for current_number_for_check in range_for_check:
    prime = True
    for curruent_deliter in range(2, current_number_for_check):
        if current_number_for_check % curruent_deliter == 0:
            prime = False
            print("Число {} cоставное".format(current_number_for_check))
            break
    if prime == True:
        print("Число {} простое".format(current_number_for_check))
