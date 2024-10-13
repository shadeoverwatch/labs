#Функция enumerate
l = [34, 'sd', 56, 34.34]

for index, element in enumerate(l):
    print(f"Индекс {index}: Элемент {element}")




#Использование срезов
my_list = [3.4, 56, "Some", "Hi", 7, 3.8, 44]

result = my_list[0:-1:3]

print(result)

#Использование индексов
my_list = [3.4, 56, "Some", "Hi", 7, 3.8, 44]

third_from_end = my_list[-3]

print(third_from_end)


#Работа с кортежами
my_tuple = (5, 10, "Hello", 3.14)
index=0
while index < len(my_tuple):
    print(my_tuple[index])
    index += 1



#Создание кортежа
tuplee = (3.14, 2.71, 42, 7, "Hello", "World")

print(tuplee)


#Кортеж из слова
my_tuple = tuple("Привет мир!")  

for char in my_tuple:
    print(char)



#Вывод элементов
tup = (3.4, 56, "Some", "Hi", 7, 3.8, 44)

third_from_end = tup[-3]
print("Третий элемент с конца:", third_from_end)

every_second_from_third = tup[2::2]
print("Каждый второй элемент, начиная с третьего:", every_second_from_third)



