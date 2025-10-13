# https://codeforces.com/group/MWSDmqGsZm/contest/223205/problem/G

from functools import reduce

inp = int(input())
numbers = input()
numbers_split = numbers.split()

numbers = [int(x) for x in numbers_split]

# max_num = reduce(lambda x, y : x if x > y else y, numbers)
# min_num = reduce(lambda x, y : x if x < y else y, numbers)

max_num = lambda x,y : x if x > y else y
print(max_num(10, 20, 30))

#print(min_num, max_num)