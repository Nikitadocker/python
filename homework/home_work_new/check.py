# 4. С клавиатуры вводятся n чисел. 
# Составьте программу, которая определяет кол-во отрицательных, кол-во положительных и кол-во нулей среди введеных чисел.Значение n вводится с клавиатуры.


number1 = int(input())
number2 = int(input())
number3 = int(input())

if number1 < 0:
    print ("Число {} отрицательное".format(number1))
elif number1 > 0:
    print ("Число {} положительное".format(number1))
elif number1 == 0:
    print ("Число {} является нулем".format(number1))
    
if number2 < 0:
    print ("Число {} отрицательное".format(number2))
elif number2 > 0:
    print ("Число {} положительное".format(number2))
elif number2 == 0:
    print ("Число {} является нулем".format(number2))
    
if number3 < 0:
    print ("Число {} отрицательное".format(number3))
elif number3 > 0:
    print ("Число {} положительное".format(number3))
elif number3 == 0:
    print ("Число {} является нулем".format(number3))