#Работа со словарями
student = {
    "имя": "Иван",
    "возраст": 15,
    "средняя оценка": 4.5
}

for key, value in student.items():
    print(f"{key}: {value}")



#Кортежи вместо ключей
student_dict = {
    ("Имя"): {"Иван"}
}

first_key = list(student_dict.keys())[0]
first_value = student_dict[first_key]

print(f"Первый элемент словаря: ключ: {first_key}, значение: {first_value}")



#Генерация словаря
dict = {}

for i in range(1, 7):
    dict[i] = i ** 2 

print(dict)



#Способы создания словаря
#Через фигурные скобки
dict1 = {
    "имя": "Иван",
    "возраст": 15,
    "средняя оценка": 4.5
}

print("Словарь через фигурные скобки:", dict1)

# Создаем словарь при помощи функции dict
dict2 = dict(имя="Мария", возраст=16, средняя_оценка=4.7)

print("Словарь через функцию dict:", dict2)


# Создаем словарь с использованием метода fromkeys
keys = ["имя", "возраст", "средняя оценка"]
values = None
dict3 = dict.fromkeys(keys, values)

print("Словарь через метод fromkeys:", dict3)



#Встроенные Функции
dicttorig = {"Один": "Питон", "Два": "C++", "Три": "Java", "Четыре": "C#"}

dicttcopy = dicttorig.copy()
print("Копия словаря:", dicttcopy)

del dicttorig

dicttcopy.pop("Три")  # Удаляем ключ "Три"
print("Копия словаря после удаления ключа 'Три':", dicttcopy)

dicttcopy["Новое"] = "Kotlin"
print("Копия словаря после добавления нового элемента:", dicttcopy)


