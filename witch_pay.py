# Всем известно, что ведьмак способен одолеть любых чудовищ, однако его услуги обойдутся недешево, 
# к тому же ведьмак не принимает купюры, он принимает только чеканные монеты. 
# В мире ведьмака существуют монеты с номиналами 1,5,10,25.
price = int(input())
counter = 0
while price - 25 >= 0:
    counter += 1
    price = price - 25
while price - 10 >= 0:
    counter += 1
    price = price - 10
while price - 5 >= 0:
    counter += 1
    price = price - 5
while price - 1 >= 0:
    counter += 1
    price = price - 1
print(counter)