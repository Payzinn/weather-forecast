# Weather App

## Технологии
Flask: Веб-фреймворк для создания приложения.
Weatherbit API: API для получения прогноза погоды.
DaData API: API для автодополнения названия города.
SQLite3: БД для хранения истории запросов.
Docker: Для контейнеризации приложения.
unittest: Для написания тестов.


Приложение можно запустить с помощью Docker, командой:

```bash
sudo docker run -p 5000:5000 -e WEATHER_API_KEY=your_api_key_here weather-app
```
Замените your_api_key_here на ваш API ключ для Weatherbit.



## Установите зависимости:

```bash
pip install -r requirements.txt
```
Запуск Flask приложения:

```bash
python app.py
```

## Тестирование
Для запуска тестов используйте unittest:


```bash
python -m unittest discover -s tests
```

## Переменные окружения
хранятся в файле .env