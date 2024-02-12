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
    # # Извлечь NAME PID из десятого столбца
    name_pid = fields[10]

    # Добавить PID в список
    pids.append(int(pid))
    
    # Добавить NAME PID в список
    name_pids.append(name_pid)
    



result = {}

for pid_for_check in pids:
    result[pid_for_check]='Prime'
    deviders = range(2, int(math.sqrt(pid_for_check) + 1))                             
    for current_devider in deviders:
        if pid_for_check % current_devider == 0:
            result[pid_for_check]='Composite'
            break
        else:
            result[pid_for_check]='Prime'


with open ('output.json', 'w') as file:
    json.dump(result, file)
    
result_name_pids = {}

for name in name_pids:
    result_name_pids[name]='name_process'
    
with open ('output_name.json', 'w') as file_name:
    json.dump(result_name_pids, file_name)