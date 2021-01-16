# Напишите программу,которая считывает последовательность из 10 целых чисел
# и определяет является ли каждое из них четным или нет.
counter = 0
for i in range (10):
    n = int(input())
    if n % 2 == 0:
        counter += 1
if counter == 10:
    print('YES')
else:
    print('NO')