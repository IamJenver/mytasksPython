# Дан список .получите новый список, в котором каждое значение будет удвоено
l1 = []
n = int(input('Input number of elements: '))
for i in range(0, n):
    el = int(input())
    l1.append(el)
p = int(input('Input multiplicator: '))
print(l1)
l2 = l1
for i in range(len(l2)):
    l2[i] *= p
print(l2)