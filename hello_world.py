# Дана строка "Hello world". Проверьте есть ли в этой строке символ пробела - " ", 
# тогда преобразуйте строку к верхнему регистру, если же нет - тогда к нижнему.
line = input('Input text: ')
item = input('What kind of symbol need to be found?: ')
if item in line:
    print(line.upper())
else:
    print(line.lower())