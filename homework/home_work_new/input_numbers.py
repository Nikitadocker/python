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

numbers =  input('Введите числа через пробел')

order = list(map(int,numbers.split()))

negative_numbers = 0
positive_numbers = 0
zero_numbers = 0

for number_for_check in order:
    if number_for_check < 0:
       negative_numbers +=1
    elif number_for_check > 0:
        positive_numbers +=1
    elif number_for_check == 0:
         zero_numbers +=1
        
        
        
       
        # count_negative_numbers = order.count(True) 
        # negative_numbers = []
        # negative_numbers.append(number_for_check)
        # len(negative_numbers)
        # sum (int(negative_numbers))
print('Количество отрицательныx чисел', negative_numbers)
print('Количество положительных чисел', positive_numbers)
print('Количество нулей', zero_numbers)
        
    # if number_for_check > 0:
    #     positive_numbers = True
    #     print('Число пожительное')
    # if number_for_check == 0:
    #     zero_numbers = True
    #     print('Число равно 0')
    