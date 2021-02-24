9# Дан массив, в котором среди прочих элементов есть слово "odd". Определите, есть ли в списке число, которое является индексом элемента "odd". 
# Напишите фукцию, которая будет возвращать True или False, соответственно.
arr = ["even", 4, "even", 7, "even", 4, "even", 55, "even", 9, "odd", 3, "even"]

def odd_ball(arr):
    for item in arr:
        if arr.index("odd") == item:
            return True
    else:
        return False

print(odd_ball(arr))
