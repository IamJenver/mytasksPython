
# Напишите программу, которая считывает 10 чисел и выводит произведение отличных от нуля чисел.
counter = 1
for i in range(10):
    n = int(input())
    if n != 0:
        counter *= n
print(counter)
