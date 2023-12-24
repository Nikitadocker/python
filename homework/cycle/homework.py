import sys
start_range = input()

finish_range = int(input())

numbers = {1: "один", 2: "два", 3: "три", 4: "четыре", 5: "пять", 6: "шесть", 7: "cемь", 8: "восемь", 9: "девять", 10: "десять"}

if start_range == "один":
    print("Последовательность простых чисел начинаеться с 2")
    sys.exit()
elif start_range == "два":
    print ("Число 2 являеться простым. Данный алгорит подходит для проверки диапозона,начиная с 3")
    sys.exit()
elif start_range == "три":
    start_range = 3
elif start_range == "четыре":
    start_range = 4
elif start_range == "пять":
    start_range = 5
# else:
#     sys.exit("Неподдержимое слово")

    
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