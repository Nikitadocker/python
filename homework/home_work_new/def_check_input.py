def check_input (start_range,finish_range):
    try:
        start_number = int(input())
        finish_number = int(input())
        if start_number > finish_number:
            raise ValueError 
        if start_number == 0 or finish_number == 0:
            raise SyntaxError
    except ValueError:
        print('Начало диапозона должно быть меньше ,чем конец диапозона')
    except SyntaxError:
        print('Ноль не может быть простым числом')
            