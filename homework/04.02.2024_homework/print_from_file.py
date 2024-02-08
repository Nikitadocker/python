# file = open('numbers.txt', 'r')
# print(file.read())
# file.close()

# file = open('numbers.json', 'r')
# print(file.read())
# file.close()

# import json
# with open('numbers.json', 'r') as file:
#     numbers = json.load(file) # json.load считывает файл json и возвращает как обьект python(в данном случае это dictionary)
#     print(type(numbers))
    
    
import json
with open('numbers.json', 'r') as file:
    numbers = json.load(file) # json.load считывает файл json и возвращает как обьект python(в данном случае это dictionary)
    start_number = numbers["start_number"]  # получаем значение по ключу из dictionary
    finish_number = numbers["finish_number"] # получаем значение по ключу из dictionary
    
    print (numbers["start_number"])
    print (numbers["finish_number"])
    
   