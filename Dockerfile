FROM python:3.8-slim

# Устанавливаем зависимости
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Устанавливаем geckodriver
RUN apt-get update && apt-get install -y firefox-esr

# Копируем geckodriver в /usr/local/bin
COPY geckodriver.exe /usr/local/bin/geckodriver

# Копируем исходный код приложения
COPY . .

# Опционально: Если вам нужны дополнительные зависимости (например, драйверы для браузера Selenium), установите их здесь.

# Определяем команду для запуска автотестов
CMD ["pytest", "tests_api.py"]