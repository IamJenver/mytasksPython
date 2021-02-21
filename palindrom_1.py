# Дан список my_str. Составьте из него список палиндромов. 
my_str = ['Око за око', 'А роза упала на лапу Азора', 'Около Миши молоко']
palindrome = []
for el in my_str:
    el_r = el.replace(' ', '').lower()
    if el_r[::-1] == el_r:
        palindrome.append(el)
print(palindrome)