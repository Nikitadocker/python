import sys
numbers = {
    '1' : 'один',
    '2' : 'два',
    '3' : 'три',
    '4' : 'четыре',
    '5' : 'пять',
    '6' : 'шесть',
    '7' : 'семь',
    '8' : 'восемь',
    '9' : 'девять',
    '10': 'десять'
}



start_range_word = input("Введите начальное число словами: ").lower().strip()
finish_range_word = input("Введите конечное число словами: ").lower().strip()

start_range = None
finish_range = None

for key, value in numbers.items():
    if start_range_word == value:
     start_range_word = key
    
    if finish_range_word == value:
        finish_range_word = key

if start_range is not None and finish_range is not None:
    for number_for_check in range (start_range, finish_range + 1):
        prime = True
        for devider in range (2, finish_range):
            if number_for_check % devider == 0:
                prime = False
                break
        if prime:
            print ( "Число {} простое ".format(number_for_check))
        else:
            print ( "Число {} cоставное ".format(number_for_check))
else:
    print('Неподдерживоемое слово. Программа завершена')
    sys.exit()
    
  
    