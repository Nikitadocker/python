import time
import os

# Чтение значения переменной окружения
app_version = os.environ.get('APP_VERSION', 'unknown')

while True:
    print(f'Hi! I have version {app_version}')
    time.sleep(10)
