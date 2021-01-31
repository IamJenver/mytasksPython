# к тому же ведьмак не принимает купюры, он принимает только чеканные монеты. 
# В мире ведьмака существуют монеты с номиналами 1, 5, 10, 25.
# Напишите программу, которая определяет какое минимальное количество чеканных монет нужно заплатить ведьмаку.
price = int(input())
counter, amount = 0, 0
<<<<<<< HEAD
exist_nominals = [1, 5, 25, 10, 50, 100]
=======
exist_nominals = [1, 5, 25, 10]
>>>>>>> ea9e3f975e2354deee7a0c0118c8c7156acc417d
exist_nominals.sort(reverse = True)
for coin in exist_nominals:
        amount = price // coin
        counter += amount
        price -= coin * amount
        print(coin, ' - ', amount)
print('total:', counter)