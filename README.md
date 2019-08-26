# OTUS Simple WSGI server
Простейший WSGI сервер. 

Создан в рамках третьего домашнего задания по курсу OTUS Web Developer.

Реализовано:
* возврат различных ответов в зависимости от запрашиваемого ресурса 
* для каждого пути доступно указание поддерживаемых методов
* поддержка jinja шаблонов


## Требования

* Python >= 3.6
* jinja2

## Установка
```
$ git clone https://github.com/AlexanderTulakin/OTUS-simple-wsgi.git
$ pip install -r requirements.txt 
```

## Запуск

Пример запуска uWSGI сервера:
```
$ uwsgi --http :8080 --wsgi-file app.py
```

## Вызов

Пример вызова:

http://127.0.0.1:8082/example_page