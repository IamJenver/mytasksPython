# Дан список words. Составьте из него список слов палиндромов. 
words = ['мадам', 'топот', 'test', 'madam', 'word']
palindrome = []
for el in words:
    if el[::-1] == el:
        palindrome.append(el)
print(palindrome)