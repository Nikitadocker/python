def check_input(start_number, finish_number):
        while start_number < 2 or finish_number < 2:
            print("Простые числа не могу быть меньше 2 Повторите ввод")
            start_number = int(input())
            finish_number = int(input())
        while start_number > finish_number:
            print("Конец диапозона должен быть больше чем начало диапозона Повторите ввод")
            start_number = int(input())
            finish_number = int(input())
        while start_number == finish_number:
            print("Начало диапозона и конец диапозона совпадают Повторите ввод")
            start_number = int(input())
            finish_number = int(input())
   

