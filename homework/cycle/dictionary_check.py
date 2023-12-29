import sys
numbers = {
    1:'один',
    2:'два',
    3:'три',
    4: 'четыре',
    5: 'пять',
    6 : 'шесть',
    7 : 'cемь',
    8 : 'восемь',
    9 : 'девять',
    10 : 'десять'
}


start_range_word = input()

finish_range_word = input()

start_range = None

finish_range = None

for key, values in numbers.items():
    if start_range_word == values:
        start_range = key
    if finish_range_word == values:
        finish_range = key

if start_range == 1:
    print ('Число 1 нельзя проверить на чистоту')
    sys.exit()

if start_range is not None and finish_range is not None:
    for number_for_check in range (start_range, finish_range +1):
        prime = True
        for divider in range (2, number_for_check):
            if number_for_check % divider == 0:
                prime = False
                break
        if prime:
            print("Число {} простое ".format(number_for_check)) 
        else:
            print("Число {} cложное ".format(number_for_check)) 
                             
else:
    print('Неподдерживаемое слово. Завершение программы')
    sys.exit()