# На вход программе подается три натуральных числа m, p, n:
# m: стартовое количество организмов;
# p: среднесуточное увеличение в %;
# n: количество дней для размножения.
# Напишите программу, которая предсказывает размер популяции организмов.
# Программа должна выводить размер популяции в каждый день, начиная с 1 и заканчивая n-м днем.
m, p, n = int(input()), int(input()), int(input())
for i in range(n):
    print(i + 1, m)
    m = m * (1 + p / 100)