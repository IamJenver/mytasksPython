# Дано натуральное число (n>9). Напишите программу, которая определяет его вторую (с начала) цифру.
num = int(input())
while num > 9:
    last_digit = num % 10
    num = num // 10
print(last_digit)