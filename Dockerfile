# Используем официальный образ Python 3.9 как базовый
FROM python:3.9-slim-buster

# Устанавливаем рабочую директорию в контейнере
WORKDIR /app

# Копируем requirements.txt в контейнер
COPY requirements.txt .

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копируем весь код проекта в контейнер
COPY . .

# Указываем порт, который будет прослушиваться контейнером (опционально, но полезно)
EXPOSE 8000

# Команда для запуска приложения
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]