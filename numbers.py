# Даны два целых числа m и n (m≤n).
# Напишите программу, которая выводит все числа от mm до nn включительно.
m, n = int(input()), int(input())
if m > n:
    for i in range(m, n + 1):
        print(i)