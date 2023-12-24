import sys
start_range = input()

finish_range = int(input())

if start_range == "один":
    print("анус")
    sys.exit()
# elif int(start_range) < 2:
#     print("анус")
#     sys.exit()
elif start_range == "два":
    start_range = 2
elif start_range == "три":
    start_range = 3
elif start_range == "четыре":
    start_range = 4
elif start_range == "пять":
    start_range = 5


    
else:
    start_range = int(start_range)


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
        print("Число {} простое".format(number_for_check))
    else:
        print("Число {} cоставное".format(number_for_check))
    number_for_check += 1
