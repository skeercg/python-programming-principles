from math import tan, pi

n = float(input())
l = float(input())

apothem = l * (1 / tan(pi / n)) / 2
print(apothem * n * l / 2)
