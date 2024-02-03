# start_number = int(input())
# finish_number = int(input())


def check_prime (start_number, finish_number):
    for number_for_check in range (start_number, finish_number +1):
        prime = True
        for deliter in range (2, number_for_check):
            if number_for_check % deliter == 0:
                prime = False
                print("Число {} составное".format(number_for_check))
                break
        if prime == True:
            print("Число {} простое".format(number_for_check))
        
    
    
    
check_prime(3, 10)
