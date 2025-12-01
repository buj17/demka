## Инструкция по запуску проекта

### Необходимые зависимости
- Python3 (желательно 3.13)
- PostgreSQL сервер

## Необходимые действия для запуска проекта на ОС Windows в Powershell

### Склонировать репозиторий
```powershell
git clone https://github.com/buj17/demka
```

### Перейти в директорию с проектом
```powershell
cd demka
```

### Создать виртуальное окружение
```powershell
python -m venv .venv
```

### Активировать виртуальное окружение
```powershell
.\.venv\Scripts\activate
```

### Установить зависимости
```powershell
pip install -r .\requirements.txt
```

### Скопировать и настроить файл с переменными окружения
```powershell
cp .\template.env .\.env
```

### Перейти в основную директорию проекта
```powershell
cd .\shoe_store\
```

### На PostgreSQL сервере необходимо создать базу данных с тем названием, которое было задано в .env файле
```postgresql
CREATE DATABASE your_db_name;
```

### Применить миграции
```powershell
alembic upgrade head
```

### Загрузить данные в БД
```powershell
python .\load_data.py
```

### Запустить приложение
```powershell
python .\main.py
```
