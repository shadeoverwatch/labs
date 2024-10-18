#Чтение и подсчет строк
file_path = "lab8_1.txt"

with open(file_path, "r") as file:
    lines = file.readlines()
    line_count = len(lines)

print(f"Количество строк в файле: {line_count}")


#Слова в файле
from collections import Counter

def count_unique_words(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        text = file.read().lower()
        words = text.split()

        words = [word.strip('.,!?"\'()') for word in words]
        
        word_count = Counter(words)
        
    return word_count

file_path = "lab8_2.txt"


word_count = count_unique_words(file_path)

print("Список уникальных слов и их количество появлений:")
for word, count in word_count.items():
    print(f"'{word}': {count}")



#Копирование файла
def copy_file(source_file, target_file):
    try:
        with open(source_file, "r", encoding="utf-8") as src:
            content = src.read()
        
        with open(target_file, "w", encoding="utf-8") as tgt:
            tgt.write(content)
        
        print(f"Содержимое файла '{source_file}' успешно скопировано в файл '{target_file}'.")
    
    except FileNotFoundError:
        print(f"Файл '{source_file}' не найден.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

source_file = "source.txt"
target_file = "target.txt"


copy_file(source_file, target_file)



#Объединение файлов
def merge_files(source_files, target_file):
    try:
        with open(target_file, "w", encoding="utf-8") as tgt:
            for file_name in source_files:
                try:
                    with open(file_name, "r", encoding="utf-8") as src:
                        content = src.read()
                        tgt.write(content + "\n")
                    print(f"Содержимое файла '{file_name}' добавлено в '{target_file}'.")
                except FileNotFoundError:
                    print(f"Файл '{file_name}' не найден.")
                except Exception as e:
                    print(f"Ошибка при обработке файла '{file_name}': {e}")
        print(f"Объединение файлов завершено. Содержимое сохранено в '{target_file}'.")
    
    except Exception as e:
        print(f"Произошла ошибка при создании целевого файла: {e}")

source_files = ["file1.txt", "file2.txt", "file3.txt"]
target_file = "merged.txt"

with open("file1.txt", "w", encoding="utf-8") as file:
    file.write("Это содержимое первого файла.")
with open("file2.txt", "w", encoding="utf-8") as file:
    file.write("Это содержимое второго файла.")
with open("file3.txt", "w", encoding="utf-8") as file:
    file.write("Это содержимое третьего файла.")

merge_files(source_files, target_file)



#Поиск и замена
def search_and_replace(file_path, search_word, replace_word):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()
        
        if search_word not in content:
            print(f"Слово '{search_word}' не найдено в файле '{file_path}'.")
            return

        updated_content = content.replace(search_word, replace_word)
        
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(updated_content)
        
        print(f"Все вхождения слова '{search_word}' заменены на '{replace_word}' в файле '{file_path}'.")
    
    except FileNotFoundError:
        print(f"Файл '{file_path}' не найден.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

file_path = "example.txt"
search_word = "Привет"
replace_word = "Здравствуйте"

with open(file_path, "w", encoding="utf-8") as file:
    file.write("Привет, мир! Привет всем!\n")

search_and_replace(file_path, search_word, replace_word)



#Обработка CSV-файлов
import csv

csv_file_path = "data.csv"
with open(csv_file_path, mode="w", encoding="utf-8", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Имя", "Возраст", "Город"])
    writer.writerow(["Иван", "25", "Москва"])
    writer.writerow(["Анна", "30", "Санкт-Петербург"])
    writer.writerow(["Олег", "22", "Новосибирск"])
    writer.writerow(["Мария", "28", "Екатеринбург"])

formatted_data = []
with open(csv_file_path, mode="r", encoding="utf-8") as file:
    reader = csv.reader(file)
    headers = next(reader)
    for row in reader:
        formatted_data.append(f"Имя: {row[0]}, Возраст: {row[1]}, Город: {row[2]}")

formatted_data



#Логирование
import datetime

def log_user_input(file_path):
    while True:
        user_input = input("Введите данные: ")
        
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        with open(file_path, "a", encoding="utf-8") as file:
            file.write(f"[{current_time}] {user_input}\n")
        
        print(f"Данные записаны: [{current_time}] {user_input}")

file_path = "userlog.txt"
log_user_input(file_path)











#Обратный порядок строк
def reverse_file_lines(source_file, target_file):
    try:
        with open(source_file, "r", encoding="utf-8") as file:
            lines = file.readlines()
        
        with open(target_file, "w", encoding="utf-8") as file:
            for line in reversed(lines):
                file.write(line)
        
        print(f"Строки из файла '{source_file}' записаны в обратном порядке в '{target_file}'.")
    
    except Exception as e:
        print(f"Произошла ошибка: {e}")

source_file = "orig.txt"
target_file = "rever.txt"

with open(source_file, "w", encoding="utf-8") as file:
    file.write("Первая строка\n")
    file.write("Вторая строка\n")
    file.write("Третья строка\n")

reverse_file_lines(source_file, target_file)



#Зашифрованный дневник
def encrypt(text, shift=3):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            encrypted_text += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            encrypted_text += char
    return encrypted_text

def decrypt(text, shift=3):
    decrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            decrypted_text += chr((ord(char) - shift_base - shift) % 26 + shift_base)
        else:
            decrypted_text += char
    return decrypted_text

def add_entry(file_path):
    entry = input("Введите новую запись: ")
    encrypted_entry = encrypt(entry)
    
    with open(file_path, "a", encoding="utf-8") as file:
        file.write(encrypted_entry + "\n")
    
    print("Запись успешно добавлена и зашифрована.")

def read_entries(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            encrypted_entries = file.readlines()
        
        print("Ваши записи:")
        for encrypted_entry in encrypted_entries:
            print(decrypt(encrypted_entry.strip()))
    
    except FileNotFoundError:
        print(f"Файл '{file_path}' не найден.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

def diary():
    file_path = "diary.txt"
    
    while True:
        print("\n--- Дневник ---")
        print("1. Добавить запись")
        print("2. Прочитать записи")
        print("3. Выйти")
        choice = input("Выберите действие: ")

        if choice == "1":
            add_entry(file_path)
        elif choice == "2":
            read_entries(file_path)
        elif choice == "3":
            print("Выход из программы.")
            break
        else:
            print("Неверный выбор, попробуйте снова.")

diary()



#Статистика файла
import re

def analyze_text_file(file_path):
    char_count = 0
    word_count = 0
    sentence_count = 0
    total_word_length = 0
    
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
        
        char_count = len(text)
        
        words = re.findall(r'\b\w+\b', text)
        word_count = len(words)
        total_word_length = sum(len(word) for word in words)

        sentence_count = len(re.findall(r'[.!?]+', text))
    
    average_word_length = total_word_length / word_count if word_count > 0 else 0

    print(f'Количество символов: {char_count}')
    print(f'Количество слов: {word_count}')
    print(f'Количество предложений: {sentence_count}')
    print(f'Средняя длина слова: {average_word_length:.2f}')

file_path = 'stat.txt'

with open(file_path, "w", encoding="utf-8") as file:
    file.write("Первая строка\n")
    file.write("Вторая строка\n")
    file.write("Третья строка\n")

analyze_text_file(file_path)
