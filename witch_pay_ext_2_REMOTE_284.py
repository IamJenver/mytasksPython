# к тому же ведьмак не принимает купюры, он принимает только чеканные монеты. 
# В мире ведьмака существуют монеты с номиналами 1, 5, 10, 25.
# Напишите программу, которая определяет какое минимальное количество чеканных монет нужно заплатить ведьмаку.
price = int(input())
counter, amount = 0, 0
exist_nominals = [1, 5, 25, 10]
exist_nominals.sort(reverse = True)
for coin in exist_nominals:
        amount = price // coin
        counter += amount
        price -= coin * amount
        print(coin, ' - ', amount)
print('total:', counter)