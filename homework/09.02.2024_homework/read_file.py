import json
from check_prime import check_prime

with open ('output_pids.json', 'r+') as file:

    file_check = json.load(file)  # <class 'list'>
    
   


for key in file_check:
    prime_or_composite = key["Prime or Composite"]
    
    pid_for_check = key["pid_number"]
    
    result_after_check = check_prime (int(pid_for_check))
    
    if result_after_check == "Prime" and prime_or_composite != "Prime":
        print("Число, {} проверено. Найдена ошибка. Число должно быть простым".format(pid_for_check))
    elif result_after_check == "Composite" and prime_or_composite != "Composite":
        print("Число, {} проверено. Найдена ошибка. Число должно быть составным".format(pid_for_check))
    elif prime_or_composite == "Not Prime and Composite":
        print("Цифра 1 является уникальной. Это не ошибка")
        
    
    
   
    