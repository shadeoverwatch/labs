def sieve_of_eratosthenes(N):
    primes = [True] * (N + 1)
    p = 2
    while p * p <= N:
        if primes[p]:
            for i in range(p * p, N + 1, p):
                primes[i] = False
        p += 1
    return [p for p in range(2, N + 1) if primes[p]]

N = 50
prime_numbers = sieve_of_eratosthenes(N)
print(f"Простые числа до {N}: {prime_numbers}")


#
a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))

if a % 2 == 0:
    print(f"Четное число: {a}")
else:
    print(f"Четное число: {b}")

#
num1 = float(input("Первое число: "))
operation = input("Операция (+, -, *, /): ")
num2 = float(input("Второе число: "))

if operation == '+':
    result = num1 + num2
elif operation == '-':
    result = num1 - num2
elif operation == '*':
    result = num1 * num2
elif operation == '/':
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Ошибка! Деление на ноль."
else:
    result = "Неверная операция!"

print(f"Результат: {result}")


#
x = 14

result = (x > 10 and x != 12 and x <= 15) or x == 18
print(result)
