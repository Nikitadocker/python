# Натуральное число, большее 1, называется простым, если оно ни на что не делится, кроме себя и 1.

# Другими словами, n > 1 – простое, если при его делении на любое число кроме 1 и n есть остаток.

# Например, 5 это простое число, оно не может быть разделено без остатка на 2, 3 и 4.

# Напишите код, который выводит все простые числа из интервала от 2 до n.

# Для n = 10 результат должен быть 2,3,5,7.

# P.S. Код также должен легко модифицироваться для любых других интервалов.



import math # импортирую библиотеку что бы использовать мат функции
# math.sqrt вернуть корень числа

# для проверки числа на простоту  мы делим число на ряд чисел до корня исследумое числа
# пример корень из 9 равен 3
# для проверки 9 на простоту мы должны разделить 9 на число 2, а потом на число 3, и проверить наличие нулевого остатка

stard = 2 # определяю начало диапозона
finishd = 10 # определяю конец диапозона
currentnumber = stard # определяю что делимое из цикла будет равно началу диапозона
delitel = stard # определяю что делитель из цикла будет равно началу диапозона

while currentnumber >= stard and currentnumber <= finishd: # делимое должно быть равно началу диапозона и не быть больше его конца
    currentnumber = currentnumber + 1
    while delitel >= stard and delitel <= math.sqrt(currentnumber): # делитель должен быть равен началу диапозон и не превашать корень делимого
        delitel = delitel + 1
    if currentnumber % delitel == 0: # если результат деления имеет нулевой остаток, значит число не является простым, и выаодить мы его не будем
            continue
            
    print(currentnumber)
