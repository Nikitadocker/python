
list_of_numbers_to_check_prime = range(4, 10)


for number_for_check_if_it_is_prime in list_of_numbers_to_check_prime:
    prime = True
    for current_delimetr in range(2, number_for_check_if_it_is_prime):
        if number_for_check_if_it_is_prime % current_delimetr == 0:
            prime = False
            print("Число  {} составное".format(
                number_for_check_if_it_is_prime))
            break

    if prime == True:
        print("Число  {} простое".format(number_for_check_if_it_is_prime))
