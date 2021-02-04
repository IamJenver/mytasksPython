# Дано натуральное число. Напишите программу, которая определяет, состоит ли указанное число из одинаковых цифр.
num = int(input())
flag = True
sample = num % 10
while num != 0:
    last_digit = num % 10
    if sample != last_digit:
        flag = False
    num = num // 10
if flag == True:
    print('YES')
else:
    print('NO')