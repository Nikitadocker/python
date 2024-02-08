from check_prime_module import check_prime
from check_input_module import check_input
import json


# input_is_good = False
# while input_is_good == False:

with open('numbers.json', 'r') as file:
        numbers = json.load(file) # json.load считывает файл json и возвращает как обьект python(в данном случае это dictionary)
        start_number = numbers["start_number"]  # получаем значение по ключу из dictionary
        finish_number = numbers["finish_number"] # получаем значение по ключу из dictionary
        input_is_good = check_input(start_number,finish_number)
        
        if input_is_good == True:
            check_prime(start_number, finish_number)
            
        
        # input_is_good = check_input(start_number,finish_number)
   
    
    
