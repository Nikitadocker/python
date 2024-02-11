import subprocess
import json
import math

result = subprocess.run(['ps', 'aux', '--no-headers'], capture_output=True, text=True)

pids = []

for line in result.stdout.splitlines():
    # Разделить строку по пробелам
    fields = line.split()
    # Извлечь PID из второго столбца
    pid = fields[1]
    # Добавить PID в список
    pids.append(int(pid))

result = {}

for pid_for_check in pids:
    deviders = range(2, int(math.sqrt(pid_for_check) + 1))                             
    for current_devider in deviders:
        if pid_for_check % current_devider == 0:
            result[pid_for_check]='Composite'
            break
        else:
            result[pid_for_check]='Prime'


with open ('output.json', 'w', encoding='utf-8') as file:
    json.dump(result, file)
    
    #  for i in range(2, int(math.sqrt(n) + 1)):