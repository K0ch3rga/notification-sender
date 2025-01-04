FROM python:3.12-slim

# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /app

# Копируем файл requirements.txt в рабочую директорию
COPY requirements.txt /app/

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копируем все файлы проекта в рабочую директорию
COPY . /app/

# Устанавливаем переменные окружения (опционально)
ENV PYTHONUNBUFFERED=1

# Определяем команду для запуска приложения
CMD ["python", "main.py"]