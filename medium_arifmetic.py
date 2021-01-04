a1, a2, a3 = input(), input(), input()
if len(a1) == (len(a2) + len(a3)) / 2 or len(a2) == (len(a1) + len(a3)) / 2 or len(a3) == (len(a2) + len(a1)) / 2:
    print('YES')
else:
    print('NO')