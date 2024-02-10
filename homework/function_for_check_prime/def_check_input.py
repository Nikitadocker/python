import sys
        
def check_input():
    try:
        start_number = int(input("Введите начальное число: "))
        finish_number = int(input("Введите конечное число: "))
        if start_number > finish_number:
            raise ValueError 
        if start_number == 0 or finish_number == 0:
            raise SyntaxError
        return start_number, finish_number
    except ValueError:
        print('Начало диапазона должно быть меньше, чем конец диапазона')
        sys.exit()
    except SyntaxError:
        print('Ноль не может быть простым числом')
        sys.exit()
