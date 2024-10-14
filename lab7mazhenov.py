#Сумма элементов списка
def sum_of_elements(numbers):

    total_sum = sum(numbers)
    return total_sum

numbers_list = [1, 2, 3, 4, 5]
result = sum_of_elements(numbers_list)
print("Сумма элементов списка:", result)


#Поиск максимального элемента
def findmaxelement(numbers):

    if not numbers:
        raise ValueError("Список не должен быть пустым.")
    
    max_element = max(numbers)
    return max_element

numbers_list = [1, 2, 3, 4, 5]
result = findmaxelement(numbers_list)
print("Наибольший элемент списка:", result)


#Генерация числовой последовательности
def createrange(start, end):

    return list(range(start, end))

startvalue = 3
endvalue = 10
result = createrange(startvalue, endvalue)
print("Список чисел в диапазоне:", result)


#Факториал числа
def factorial(n):
    if n < 0:
        raise ValueError("Факториал определен только для неотрицательных чисел.")
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

number = 7
result = factorial(number)
print(f"Факториал числа {number}:", result)


#Подсчет количества гласных
def countvow(string):
 
    vows = "аеёиоуыэюяАЕЁИОУЫЭЮЯ"
    count = sum(1 for char in string if char in vows)
    return count

string = "Меня зову Даниель"
result = countvow(string)
print(f"Количество гласных в строке: {result}")


#Функция для вычисления среднего
def calculate_average(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

numbers_list = [10, 20, 30, 40, 50]
average = calculate_average(numbers_list)
print(f"Среднее значение списка: {average}")



#Функция для поиска наибольшей буквы
def find_largest_letter(string):
    letters = [char for char in string if char.isalpha()]
    
    if not letters:
        return ""
    
    return max(letters)

input_string = "Привет, как дела?"
largest_letter = find_largest_letter(input_string)
print(f"Наибольшая буква в строке: {largest_letter}")


#Лямбда-функция для умножения
multiply = lambda x, y: x * y

result = multiply(5, 3)
print(result)
