

# import sys


# numbers = {1: "один", 2: "два", 3: "три", 4: "четыре", 5: "пять", 6: "шесть", 7: "cемь", 8: "восемь", 9: "девять", 10: "десять"}

# start_range = input()
# finish_range = input()

# if start_range in numbers and finish_range in numbers:
#     start_range = numbers[start_range]
#     finish_range = numbers[finish_range]
# else:
#     print("неподдерживаемое слово. Программа завершена")
#     sys.exit()
    
# for number_for_check in range (int(start_range), int(finish_range)+1):
#     prime = True
#     for deliter in range(2, number_for_check):
#         if number_for_check % deliter == 0:
#             prime = False
#             break
#     if prime:
#         print("Число {} простое".format(number_for_check))
#     else:
#         print("Число {} составное".format(number_for_check))
        
    
import sys

numbers = {1: "один", 2: "два", 3: "три", 4: "четыре", 5: "пять", 6: "шесть", 7: "семь", 8: "восемь", 9: "девять", 10: "десять"}

start_range_word = input("Введите начальное число словами: ").lower()
finish_range_word = input("Введите конечное число словами: ").lower()

start_range = None
finish_range = None

for key, value in numbers.items():
    if start_range_word == value:
        start_range = key
    if finish_range_word == value:
        finish_range = key

if start_range is not None and finish_range is not None:
    for number_for_check in range(start_range, finish_range + 1):
        prime = True
        for divisor in range(2, number_for_check):
            if number_for_check % divisor == 0:
                prime = False
                break
        if prime:
            print("Число {} простое".format(number_for_check))
        else:
            print("Число {} составное".format(number_for_check))
else:
    print("Неподдерживаемое слово. Программа завершена.")
    sys.exit()


