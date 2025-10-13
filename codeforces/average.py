# https://codeforces.com/group/MWSDmqGsZm/contest/223205/problem/J

from functools import reduce

inp = int(input())
numbers = input()
numbers_split = numbers.split()

numbers = [float(x) for x in numbers_split]

avg_val = reduce(lambda x, y: x + y, numbers)

avg_mean = avg_val / inp

print(f"{avg_mean:.7f}")