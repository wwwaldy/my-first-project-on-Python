import time
import requests

API_KEY = "6672d01dc5bd087355c42e8901fc56f7"

CITIES = [
    "Киев", "Львов", "Одесса", "Харков", "Ужгород", "Луцк", "Ровно", "Тернополь", "Ивано-Франковск",
    "Черновцы", "Житомир", "Винница", "Кропивницкий", "Полтава", "Сумы", "Чернигов", "Николаев",
    "Запорожье", "Днепр", "Донецк", "Луганск", "Херсон", "Кривой Рог", "Хмельницкий", "Черкассы",
]
print("Добро пожаловать в погоду!\n")
print("Средняя температура в Украине сейчас: ")
