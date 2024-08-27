# Aleucos 

Проект реализует функционал по загрузке данных из xlsx-файла. Загрузить данные можно, перейдя в административную панель Django и выбрав раздел Products. Там будет кнопка "Импортировать записи из XLSX".

### 1. Запуск PostgreSQL в docker-compose 

```
docker-compose up --build
``` 

### 2. Создание и активация виртуального окружения

```
# Для Windows
python -m venv venv
venv\Scripts\Activate

# Для macOS/Linux
python -m venv venv
source venv/bin/activate

``` 

### 3. Установка зависимостей

```
pip install -r requirements.txt
``` 

### 4. Применение миграций

```
python manage.py migrate
``` 

### 5. Загрузка фикстур

```
python manage.py loaddata fixtures\user.json
``` 
Будет создан суперпользователь для входа в административную панель Django: 
- username = admin 
- password = admin

### 6. Запуск проекта
Запуск Celery: 
```
celery -A Aleucos worker -l info -P solo
``` 
Запуск Flower (если необходимо): 
``` 
celery -A Aleucos flower -l info    
```  
Запуск сервера на локальной машине:

```
python manage.py runserver
``` 
Административная панель будет доступна по адресу `127.0.0.1:8000/admin`, а Flower – по адресу `127.0.0.1:5555`.