# Напишите программу, которая считывает натуральное число n
# и выводит первые nn чисел последовательности Фибоначчи.
n = int(input())
fibo = 1
pre_fibo = 1
for i in range(n):
    print(fibo)
    fibo = fibo + pre_fibo
    pre_fibo = fibo