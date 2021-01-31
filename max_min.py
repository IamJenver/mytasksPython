# Дано натуральное число n, (n≥10). Напишите программу, которая определяет его максимальную и минимальную цифры.
num = int(input())
num_max = num % 10
num_min = num % 10
while num != 0:
    last_digit = num % 10
    if last_digit > num_max:
        num_max = last_digit
    if last_digit < num_min:
        num_min = last_digit
    num = num // 10
print('Максимальная цифра равна', num_max)
print('Минимальная цифра равна', num_min)
