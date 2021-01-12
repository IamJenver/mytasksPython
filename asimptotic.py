# На вход программе подается натуральное число n. Напишите программу,
# которая вычисляет значение выражения
n = int(input())
counter = 0
from math import log
for i in range(1, n + 1):
    counter = counter + 1 / i
counter -= log(n)
print(counter)