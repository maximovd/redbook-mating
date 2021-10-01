## Технологии

Django, DRF, PostgreSQL, PostGIS, Django-allauth, djangorestframework-simplejwt
Pipenv, Pytest

## Краткое описание

Бекенд системы для случки краснокнижных животных
Для работы с геопозицией и поиска животных поблизости используется PostGIS

## Информация о деплое

Деплой стандартными средствами django

## Запуск

Перед запуском необходимо установить [pipenv](https://pipenv.pypa.io/en/latest/)

Также необходима установка PostgreSQL и PostGIS

* Создаем виртуальное окружение:
```shell
pipenv install
```
* Активируем окружение:
```shell
pipenv shell
```
* Запускаем миграции:
```shell
make migration
```
* Запускаем приложение:
```shell
python manage.py runserver
```

## Использование
По умолчанию запускается на http://127.0.0.1:8000

Документация доступа по адресу http://127.0.0.1:8000/swagger или http://127.0.0.1:8000/redoc