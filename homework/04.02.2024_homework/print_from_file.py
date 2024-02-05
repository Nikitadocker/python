# file = open('numbers.txt', 'r')
# print(file.read())
# file.close()

# file = open('numbers.json', 'r')
# print(file.read())
# file.close()

import json
with open('numbers.json', 'r') as file:
    numbers = json.load(file)
    print(numbers)