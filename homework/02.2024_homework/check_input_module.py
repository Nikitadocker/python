def check_input(start_number, finish_number):
    if start_number < 2 or finish_number < 2:
        print(' Числа меньше 2 не могут быть простыми. Повторите ввод ')
        
        return False
    elif start_number == finish_number:
        print(' Введенные значение совпадают. Повторите ввод ')
        return False
    elif start_number > finish_number:
        print('Начало диапозона не должно быть чем конец диапзона Повторите ввод')
        return False
    else: 
        return True


