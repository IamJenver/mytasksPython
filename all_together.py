# Дано натуральное число. Напишите программу, которая вычисляет:
# сумму его цифр;
# количество цифр в нем;
# произведение его цифр;
# среднее арифметическое его цифр;
# его первую цифру;
# сумму его первой и последней цифры.
# Программа должна вывести значения указанных величин в указанном порядке.
num = int(input())
saved_num = num
s_num = 0
amount_digit = 0
multipl = 1
averedge = 0
l_digit = num % 10
last = 0
while num != 0:
    last_digit = num % 10
    s_num += last_digit
    amount_digit += 1
    multipl *= last_digit
    averedge = s_num / amount_digit
    num = num // 10
    last = last_digit + l_digit
print(s_num, amount_digit, multipl, averedge, last_digit, last, sep = '\n')