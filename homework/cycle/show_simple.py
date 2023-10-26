# Натуральное число, большее 1, называется простым, если оно ни на что не делится, кроме себя и 1.

# Другими словами, n > 1 – простое, если при его делении на любое число кроме 1 и n есть остаток.

# Например, 5 это простое число, оно не может быть разделено без остатка на 2, 3 и 4.

# Напишите код, который выводит все простые числа из интервала от 2 до n.

# Для n = 10 результат должен быть 2,3,5,7.

# P.S. Код также должен легко модифицироваться для любых других интервалов.

# def add(x, y):
#     return x + y


import math # импортирую библиотеку что бы использовать мат функции
# math.sqrt вернуть корень числа

stard = 2 # определяю начало диапозона
finishd = 10 # определяю конец диапозона
currentnumber = stard

delitel = stard

while currentnumber >= stard and currentnumber <= finishd:
    currentnumber = currentnumber + 1
    while delitel >= stard and delitel <= math.sqrt(currentnumber):
        delitel = delitel + 1
    if currentnumber % delitel == 0:
            continue
            
    print(currentnumber)
