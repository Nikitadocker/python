import math

stard = 2  # начало диапазона
finishd = 10  # конец диапазона
currentnumber = stard  # начальное значение текущего числа

while currentnumber <= finishd:  # делимое должно быть равно началу диапазона и не превышать его конец
    delitel = 2  # начинаем с делителя 2
    prime = True  # устанавливаем флаг, предполагая, что число простое

    while delitel <= math.sqrt(currentnumber):
        if currentnumber % delitel == 0:
            prime = False  # если результат деления имеет нулевой остаток, число не является простым
            break  # можно прервать проверку, так как число уже не простое

        delitel += 1

    if prime:  # если флаг остался True, то число простое
        print(currentnumber)

    currentnumber += 1
