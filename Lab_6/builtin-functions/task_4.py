from math import sqrt
import time

a = float(input())
b = float(input())

time.sleep(b * 0.001)

print(f'Square root of {a} after {b} milliseconds is {sqrt(a)}')