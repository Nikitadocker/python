# Используем базовый образ с поддержкой Python
FROM python:3.8

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем исходный код приложения в контейнер
COPY . .

# Устанавливаем зависимости
# RUN pip install --no-cache-dir -r requirements.txt

# Определяем команду для запуска приложения
CMD ["python","-u","script.py"]
