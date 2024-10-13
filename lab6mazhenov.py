#Работа с множествами
set = {10, 20, 30, 40, 50}

try:
    set.remove(67)
except KeyError:
    print("67 УДАЛЕН.")

set.add(60)
set.add(70)

print("Множество после операций:", set)


#Очистка повторений
my_list = [1, 53, 8, 9, 34, 1, 0, 53, 53, 8, 73, 5]

uniqset = set(my_list)

uniqlist = list(uniqset)
print("Список без повторяющихся элементов:", uniqlist)


#Создание множества
#set
setfunct = set([1, 2, 3, 4, 5])
print("Множество из функции set():", setfunct)

#с использованием фигурных скобок
setbraces = {6, 7, 8, 9, 10}
print("Множество из фигурных скобок:", setbraces)

#с использованием цикла for
setfor = set()  # Начинаем с пустого множества

for i in range(1, 6):
    setfor.add(i)

print("Множество из цикла for:", setfor)


#Объединение
myset = {1, 3, 4, 5}
myfrozenset = frozenset({10, 20})

combinedset = myset.union(myfrozenset)
print("Объединенное множество:", combinedset)

combinedset = combinedset | {2, 5}
print("После добавления элементов 2 и 5:", combinedset)

combinedset.remove(2)
print("После удаления числа 2:", combinedset)

combinedset = set(list(combinedset)[1:])
print("После удаления первого элемента:", combinedset)
