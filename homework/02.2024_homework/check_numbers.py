print('Введите N')

N = int(input())

positive_numbers = 0

negative_numbers = 0

zero_numbers = 0

for _ in range (N):
    number = int(input())
    if number > 0:
        positive_numbers += 1
    elif number < 0:
        negative_numbers += 1
    elif number == 0:
        zero_numbers += 1
print ('Количество положительных чисел', positive_numbers)
print ('Количество  отрицательных чисел', negative_numbers)
print ('Количество нулей', zero_numbers)   
