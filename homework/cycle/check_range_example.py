


range_for_check = range(2, 11)


for current_number_for_check in range_for_check:
    prime = True
    for deliter in range(2, current_number_for_check):
        if current_number_for_check % deliter == 0:
            prime = False
            print("Число {} составное".format(current_number_for_check))
            break
    if prime == True:
        print("Число {} простое".format(current_number_for_check))

    


start_range = 2

while start_range < 11:
    prime = True
    deliter = 2
    while deliter < start_range:
        if start_range % deliter == 0:
            prime = False
            print("Число {} составное".format(start_range))
            break
        deliter +=1
    if prime == True:
        print("Число {} простое".format(start_range))
    
    
    start_range += 1
