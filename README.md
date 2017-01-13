# Функционал программы
Данная программа выводит в консоль содержимое файлов формата JSON в удобном формате (pretty print)

# Требования
Для работы с программой требуется наличие файла в формате JSON и python версии 3 или выше

# Как использовать?
Запустите скрипт с дополнительным аргументом: `-f` или `--file` путь к JSON файлу или просто название, если файл находится в директории скрипта  
**Пример:**
```
user$ python3 pprint_json.py -f data.json
```
или
```
user$ python3 pprint_json.py -f /some_directory/data.json
```
# Пример работы скрипта
Необработанные данные в формате JSON выглядят примерно так:
```
[{"Id":"79742784-9ef3-4543-bc98-a219a8903c18","Number":1,"Cells":{"global_id":14371450,"Name":"Ароматный Мир","IsNetObject":"да","OperatingCompany":"Ароматный Мир","TypeService":"реализация продовольственных товаров","AdmArea":"Западный административный округ","District":"район Кунцево","Address":"улица Академика Павлова, дом 10","PublicPhone":[{"PublicPhone":"(495) 777-51-95"}],"WorkingHours":[{"Hours":"09:30-22:30","DayOfWeek":"понедельник"},{"Hours":"09:30-22:30","DayOfWeek":"вторник"},{"Hours":"09:30-22:30","DayOfWeek":"среда"},{"Hours":"09:30-22:30","DayOfWeek":"четверг"},{"Hours":"09:30-22:30","DayOfWeek":"пятница"},{"Hours":"09:30-22:30","DayOfWeek":"суббота"},{"Hours":"09:30-22:30","DayOfWeek":"воскресенье"}],"ClarificationOfWorkingHours":null,"geoData":{"type":"Point","coordinates":[37.39703804817934,55.740999719549094]}}}, {"Id":"1bd07c21-05de-4015-b015-d22657168ded","Number":2,"Cells":{"global_id":14934782,"Name":"Массандра в Алтуфьево","IsNetObject":"да","OperatingCompany":"Массандра","TypeService":"реализация продовольственных товаров","AdmArea":"Северо-Восточный административный округ","District":"район Бибирево","Address":"улица Лескова, дом 6","PublicPhone":[{"PublicPhone":"(499) 909-40-08"}],"WorkingHours":[{"Hours":"10:00-22:00","DayOfWeek":"понедельник"},{"Hours":"10:00-22:00","DayOfWeek":"вторник"},{"Hours":"10:00-22:00","DayOfWeek":"среда"},{"Hours":"10:00-22:00","DayOfWeek":"четверг"},{"Hours":"10:00-22:00","DayOfWeek":"пятница"},{"Hours":"10:00-22:00","DayOfWeek":"суббота"},{"Hours":"10:00-22:00","DayOfWeek":"воскресенье"}],"ClarificationOfWorkingHours":null,"geoData":{"type":"Point","coordinates":[37.593177064306758,55.897722369367969]}}}]
```
Но эти данные трудно читать пользователю. Гораздо лучше читать, если данные выглядят вот так:
```
{
        "Cells": {
            "Address": "улица Академика Павлова, дом 10",
            "AdmArea": "Западный административный округ",
            "ClarificationOfWorkingHours": null,
            "District": "район Кунцево",
            "IsNetObject": "да",
            "Name": "Ароматный Мир",
            "OperatingCompany": "Ароматный Мир",
            "PublicPhone": [
                {
                    "PublicPhone": "(495) 777-51-95"
                }
            ],
            "TypeService": "реализация продовольственных товаров",
            "WorkingHours": [
                {
                    "DayOfWeek": "понедельник",
                    "Hours": "09:30-22:30"
                },
                {
                    "DayOfWeek": "вторник",
                    "Hours": "09:30-22:30"
                },
                {
                    "DayOfWeek": "среда",
                    "Hours": "09:30-22:30"
                },
                {
                    "DayOfWeek": "четверг",
                    "Hours": "09:30-22:30"
                },
                {
                    "DayOfWeek": "пятница",
                    "Hours": "09:30-22:30"
                },
                {
                    "DayOfWeek": "суббота",
                    "Hours": "09:30-22:30"
                },
                {
                    "DayOfWeek": "воскресенье",
                    "Hours": "09:30-22:30"
                }
            ],
            "geoData": {
                "coordinates": [
                    37.39703804817934,
                    55.740999719549094
                ],
                "type": "Point"
            },
            "global_id": 14371450
        },
        "Id": "79742784-9ef3-4543-bc98-a219a8903c18",
        "Number": 1
    },
```
# Кодировка 
Скрипт корректно работает с кодировкой *utf-8*

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
