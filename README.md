# API для yatube

## Описание

Яндекс практикум, проект 9 спринта.

## Что использовалось

Django, Django REST framework

## Функционал

-Просмотр постов и комментариев;
-Создание и удаление постов авторизованными пользователями;
-Просмотр групп;
-Создание и удаление комментариев к постам авторизованными пользователями;
-Возможность подписки на пользователей.

### Примеры запросов

Запрос токена.
Отправить POST запрос к 'api/v1/jwt/create/':
```
    {
        "username":"andrew",
        "password":"test_password"
    }
```
Создание поста.
Отправить POST запрос к 'api/v1/jwt/create/' с указанием JWT токена:
```
    {
        "text":"Test post",
        "group":"Test group"
    }
```

Пример ответа.
```
   {
     "id": 3,
     "author": "andrew",
     "text": "Test post",
     "pub_date": "2023-04-03T10:00:00",
     "image": null,
     "group": "Test group"
   }
```
### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/yandex-praktikum/api_final_yatube.git
```

```
cd kittygram
```

Cоздать и активировать виртуальное окружение:

```
python -m venv venv
```

```
source venv/scripts/activate
```

Установить зависимости из файла requirements.txt:

```
python -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python manage.py migrate
```

Запустить проект:

```
python manage.py runserver





