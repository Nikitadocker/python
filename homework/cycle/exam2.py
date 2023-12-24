# Спрашивать у пользователя ввод если он ввел что угодно кроме числа 10
# если прользователь ввел 10 напечать на экран все простые числа от 10 до 100
# можно использовать любые циклы


start_range = int(input())

while start_range != 10:
    start_range = int(input())
if start_range == 10:
    for number_for_check in range(10, 101):
        prime = True
        for devider in range(2, number_for_check):
            if number_for_check % devider == 0:
                prime = False
                break
        if prime:
            print("Число {} простое".format(number_for_check))

            
            
    