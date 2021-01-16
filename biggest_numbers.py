# На вход программе подается натуральное число n, 
# а затем n различных натуральных чисел, каждое на отдельной строке.
# Напишите программу, которая выводит наибольшее и второе наибольшее число последовательности.
n = int(input())
biggest = 1
second = 1
for i in range (n):
    num = int(input())
    if num > biggest:
        second = biggest
        biggest = num
        if num > second

print(biggest)
print(second)

        
    