#Работа со списками
first_list = [i for i in range(5)]

second_list = []
second_list.append(5)
second_list.append(-6)
second_list.extend(first_list)

second_list.sort()

print(f"Первый список: {first_list}")
print(f"Второй список: {second_list}")



#Создание списка пользователем
user_input = input("Введите строку: ")

char_list = [char for char in user_input]

print(char_list)


#Вывод по отдельности
listtt = ["Андрей", "Иван", "Василий", "Петро", "Максим", "Дима"]

for word in listtt:
    print(word)  
    for letter in word:
        print(letter) 

#Наименьший элемент
listt = [1, 34, 8, 0, -5, 7, 32, 74, 59, 92, 41, 10, -2]

min_element = min(listt)

listt.remove(min_element)

if min_element < 0:
    listt.append(min_element) 
else:
    listt.insert(0, min_element) 

print(listt)


#Добавление списка пользователем
some = [9, "Hi", 23.5, "A"]

N = int(input("Введите количество новых элементов для добавления в список: "))

for i in range(N):
    new_element = input(f"Введите элемент {i+1}: ")
    some.append(new_element)

print("Итоговый список:", some)




#Задача
num1 = int(input("Введите первое число: "))
num2 = int(input("Введите второе число: "))
num3 = int(input("Введите третье число: "))

numbers_list = [num1, num2, num3]
numbers_tuple = (num1, num2, num3)

print(f"Список: {numbers_list}")
print(f"Кортеж: {numbers_tuple}")

