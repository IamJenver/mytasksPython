# Дан список. Возведите в квадрат каждый из его элементов и получите сумму всех полученных квадратов
l1 = []
n = int(input('Input number of elements: '))
for i in range(0, n):
    el = int(input())
    l1.append(el)
p = int(input('Input degree: '))
print(l1)
l2 = l1
counter = 0
for j in range(len(l2)):
    l2[j] **= p
    counter += l2[j]
print(counter)