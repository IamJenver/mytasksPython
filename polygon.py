from math import tan, pi
n, a = int(input()), float(input())
s = (n * pow(a, 2)) / (4 * tan(pi / n))
print(s)