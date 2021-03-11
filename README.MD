# Тестовое задание "Тест из N вопросов"
 

Например "Угадай самолет/машину/что угодно" по картинке.
По четыре варианта ответа с одним правильным.
Если все ответы правильные, то сообщить пользователю, что "он лучший",
от 8 до 10 - "почти лучший"
от 3 до 8 - "бывает и лучше"
до 3 - "вы нуб"

Развертываение:

1)Скопировать репозиторий
2)Создать файл .env по образцу
    SECRET_KEY=
    DB_ENGINE=django.db.backends.postgresql_psycopg2
    POSTGRES_DB=
    POSTGRES_USER=
    POSTGRES_PASSWORD=
    DB_HOST=
    DB_PORT=5432
    SERVER_NAMES=*
3)docker-compose build
4)docker-compose up -d
5)docker-compose exec web bash
    python manage.py makemigrations
    python manage.py migrate
    python manage.py loaddata questions.json