n = int(input())

inp = input()
inp_split = inp.split()
numbers = [int(x) for x in inp_split]

nums = tuple(numbers)
print(hash(nums))