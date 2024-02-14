import subprocess
import json
import math

result = subprocess.run(['ps', 'aux', '--no-headers'], capture_output=True, text=True)

pids = []

name_pids = []

for line in result.stdout.splitlines():
    # Разделить строку по пробелам
    fields = line.split()
    # Извлечь PID из второго столбца
    pid = fields[1]
    
    # Извлечь NAME PID из десятого столбца
    name_pid = fields[10]
    # Добавить PID в список
    pids.append(int(pid))
    
    # Добавить NAME PID в список
    name_pids.append(name_pid)
    
    
    


# Добавление ключа "pid_number"
json_data = [{
    "pid_number": pid
} for pid in pids
             {"pid_name:" name} for name in name_pids]

# Преобразование в JSON
json_string = json.dumps(json_data)

print(json_string)   
    
# with open ('output_pids.json', 'w') as file_write_pids:
#     json.dump(json_data, file_write_pids)
    

# result = {}

# for pid_for_check in pids:
#     if pid_for_check == 2 or pid_for_check == 3:
#         result[pid_for_check] ="Prime"

            
#     else:
#         result[pid_for_check]='Not Prime and Composite'    
#         initial_devider = 2
#         final_devider = int(math.sqrt(pid_for_check))  # final_devider = 1
#         deviders = range(initial_devider, final_devider +1)  # deviders = [2]
#         for current_devider in deviders:
#             if pid_for_check % current_devider == 0:
#                 result[pid_for_check]='Composite'
#                 break
#             else:
#                 result[pid_for_check]='Prime'


# with open ('output.json', 'w') as file:
#     json.dump(result, file)
    
    



