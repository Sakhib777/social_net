# Simple Social Network API

Проект написан на Django REST Framework.

## Возможности

- Регистрация, вход и выход (JWT)
- Создание постов
- Комментирование постов
- Лайк / дизлайк постов
- Просмотр постов с количеством лайков и комментариев

## Установка и запуск

```bash
git clone <ссылка если будет>
cd <название_проекта>
python -m venv venv
source venv/bin/activate   # для Windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver