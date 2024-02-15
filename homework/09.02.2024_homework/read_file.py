import json
from dictionary import check_prime

with open ('output_pids.json', 'r') as file_read:

    file_check = json.load(file_read)  # <class 'list'>
    
    # print(type(file_check))


for key in file_check:
    prime_or_composite = key["Prime or Composite"]
    
    pid_for_check = key["pid_number"]
    
    result_after_check = check_prime (int(pid_for_check))
    
    if result_after_check == "Prime":
        prime_or_composite == "Prime"
    elif result_after_check == "Composite":
            prime_or_composite == "Composite"
    elif prime_or_composite == "Not Prime and Composite":
        print("Цифра 1 является уникальной. Это не ошибка")
        
    else:
        print("Найдена ошибка. Число должно быть Простым")
    
   
    