# Курсовой проект 5. Работа с базами данных 

## Описание 
 Проект написан на языке Python.
 С помощью данного проекта идет получение данных о компаниях и вакансиях с сайта hh.ru
 Можно спроектировать таблицы и БД PostgreSQL.
 Полученные данные загружаются в созданные таблицы.
 Также можно, используя данные из таблиц SQL, вывести в необходимом виде информацию 


## Основные шаги проекта

- Получить данные о работодателях и их вакансиях с сайта [hh.ru](http://hh.ru/). Для этого использован публичный API [hh.ru](http://hh.ru/) и библиотеку `requests`.
- Выбрано не менее 10 компаний, от из которых загружаются данные о вакансиях по API.
- Спроектированы таблицы в БД Postgres для хранения полученных данных о работодателях и их вакансиях. Для работы с БД используется библиотека `psycopg2`.
- Реализован код, который заполняет созданные таблицы в БД Postgres данными о работодателях и их вакансиях.
- Создан класс `DBManager` для работы с данными в БД.

## Класс DBManager

Создан класс `DBManager`, который будет подключаться к БД Postgres и иметь следующие методы:

- `get_companies_and_vacancies_count()`: получает список всех компаний и количество вакансий у каждой компании.
- `get_all_vacancies()`: получает список всех вакансий с указанием названия компании, названия вакансии и зарплаты и ссылки на вакансию.
- `get_avg_salary()`: получает среднюю зарплату по вакансиям.
- `get_vacancies_with_higher_salary()`: получает список всех вакансий, у которых зарплата выше средней по всем вакансиям.
- `get_vacancies_with_keyword()`: получает список всех вакансий, в названии которых содержатся переданные в метод слова, например “python”.


## Для начала работы программы необходимо:

1. Загрузить в корень проекта файл (к примеру `database.ini`) с вашими данными для входа в sql в таком виде:

        [postgresql]
        host=localhost 
        user=user_name 
        password=12345 
        port=5432

      В данных переменных указывайте свои данные.
      Описание переменных: `host`- хост, `user`- имя пользователя, `password` - пароль пользователя, `port` - порт

2. В корне проекта лежит файл - `config.py`. 
   В нем в переменную `file_exp` добавить абсолютный путь до вышесозданного файла(к примеру `database.ini`).
   Пример:
   `file_exp = "F:/python/C_w_5_postgreSQL/database.ini"`

## Работа с программой

Для работы с программой необходимо запустить `main.py` в корне проекта.
1. Нажмите "w", если файл и путь присутствуют. 
2. Далее можно загрузить данные с HH, либо работать с ранее созданной
   - Загрузка данных.
   1. Введите количество страниц для загрузки по каждому работадателю.(В каждой странице по 100 вакансий)
   2. Далее идет процесс Создания бд.
      - Введите название Новой бд
   3. Далее идет процесс Заполнение бд данными.
3. Для работы с готовой БД введите название бд
   - Далее выбираете необходимую задачу и вводите номер задачи, для выхода - 0
 
