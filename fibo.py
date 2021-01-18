# Напишите программу, которая считывает натуральное число n
# и выводит первые n чисел последовательности Фибоначчи.
n = int(input())
fibo = 1
first = second = 0
if n < 2:
    print('1')
else:
    for i in range(n):
        print(fibo, end = ' ')
        second, first = first, fibo
        fibo = first + second
        
    
    