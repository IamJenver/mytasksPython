# Напишите функцию find_sum, где аргумент функции - это конечный элемент
# последовательности включительно. Функция должна вернуть сумму  всех чисел
# последовательности, кратных 3 или 5.
l1 = []
n = int(input('Input number of elements: '))
for i in range(0, n):
    el = int(input())
    l1.append(el)

def find_sum(l1):
    cnt = 0
    for item in l1:
        if item % 3 == 0 or item % 5 == 0:
            cnt += item
    return(cnt)
print(find_sum(l1))