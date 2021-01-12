# На вход программе подается натуральное число n,
# а затем nn целых чисел, каждое на отдельной строке. 
# Напишите программу, которая подсчитывает сумму введенных чисел.
n = int(input())
counter = 0
for i in range(n):
    number = int(input())
    counter = counter + number
print(counter)