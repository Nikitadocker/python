# 4. С клавиатуры вводятся n чисел. 
# Составьте программу, которая определяет кол-во отрицательных, кол-во положительных и кол-во нулей среди введеных чисел.Значение n вводится с клавиатуры.
# 1) Пишет на экран для пользователя "Введите N"
# 2) Пользователь пишет количество чисел которое хочет набрать. В нашем случае 7
# 3) вводит желаемую комбинацию длиной в 7 чисел
# Вопросы:
# 1. Правильно ли я понял то , о чем писал выше?
# 2. Пользователь вводит числа через пробел


print("Введите N")

N = int(input())

negative_numbers = 0
positive_numbers = 0
zero_numbers = 0

for _ in range(N):
    number = input()
    if number < 0:
        negative_numbers +1
    elif number > 0:
        
        
    




for number_for_check in :
    if number_for_check < 0:
       negative_numbers +=1
    elif number_for_check > 0:
        positive_numbers +=1
    elif number_for_check == 0:
         zero_numbers +=1
        
print('Количество отрицательныx чисел', negative_numbers)
print('Количество положительных чисел', positive_numbers)
print('Количество нулей', zero_numbers)
        
