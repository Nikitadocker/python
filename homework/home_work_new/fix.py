start_range = input()
finish_range = input()

if start_range == "один":
   start_range = 1
elif start_range == "два":
    start_range = 2
elif start_range == "три":
    start_range = 3
elif start_range == "четыре":
    start_range = 4
elif start_range == "пять":
    start_range = 5
elif start_range == "шесть":
    start_range = 6
elif start_range == "cемь":
    start_range = 7
elif start_range == "воcемь":
    start_range = 8
elif start_range == "девять":
    start_range = 9
elif start_range == "десять":
    start_range = 10    
else:
    start_range = int(start_range)
    
    
if finish_range == "один":
   finish_range = 1
elif finish_range == "два":
    finish_range = 2
elif finish_range == "три":
    finish_range = 3
elif finish_range == "четыре":
    finish_range = 4
elif finish_range == "пять":
    finish_range = 5
elif finish_range == "шесть":
    finish_range = 6
elif finish_range == "cемь":
    finish_range = 7
elif finish_range == "воcемь":
    finish_range = 8
elif finish_range == "девять":
    finish_range = 9
elif finish_range == "десять":
    finish_range = 10    
else:
    finish_range = int(finish_range)



number_for_check = start_range

while number_for_check < finish_range + 1:
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