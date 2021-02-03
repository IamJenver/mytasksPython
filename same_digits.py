# Дано натуральное число. Напишите программу, которая определяет, состоит ли указанное число из одинаковых цифр.
num = int(input())
averedge = 0
counter = 0
while num != 0:
    last_digit = num % 10
    averedge += last_digit
    counter += 1
    num = num // 10
if averedge / counter == last_digit:
    print('YES')
else:
    print('NO')