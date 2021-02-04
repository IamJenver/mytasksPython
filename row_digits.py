# Дано натуральное число. Напишите программу, которая определяет, 
# является ли последовательность его цифр при просмотре справа налево упорядоченной по неубыванию.
num = int(input())
flag = True
nd_digit = num % 10
while num != 0:
    last_digit = num % 10
    if nd_digit > last_digit:
        flag = False
    nd_digit = last_digit
    num = num // 10
if flag == True:
    print('YES')
else:
    print('NO')