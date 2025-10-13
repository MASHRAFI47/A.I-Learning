# https://codeforces.com/group/MWSDmqGsZm/contest/223205/problem/G

from functools import reduce

inp = int(input())
numbers = input()
numbers_split = numbers.split()

numbers = [int(x) for x in numbers_split]

max_num = reduce(lambda x, y : x if x > y else y, numbers)
min_num = reduce(lambda x, y : x if x < y else y, numbers)

print(min_num, max_num)



# n = int(input())
# arr = list(map(int, input().split()))

# print((lambda a: min(a))(arr), (lambda a: max(a))(arr))


# find_min = lambda arr: min(arr)
# find_max = lambda arr: max(arr)


# n = int(input())
# arr = list(map(int, input().split()))

# # Output
# print(find_min(arr), find_max(arr))