first, second, therd = input(), input(), input()
m1 = min(len(first), len(second), len(therd))
m2 = max(len(first), len(second), len(therd))
if m1 == len(first) and m2 == len(second):
    print(first)
    print(second)
elif m1 == len(first) and m2 == len(therd):
    print(first)
    print(therd)
elif m1 == len(second) and m2 == len(therd):
    print(second)
    print(therd)
elif m1 == len(second) and m2 == len(first):
    print(second)
    print(first)
elif m1 == len(therd) and m2 == len(first):
    print(therd)
    print(first)
elif m1 == len(therd) and m2 == len(second):
    print(therd)
    print(second)