# https://codeforces.com/group/MWSDmqGsZm/contest/219856/problem/J

str = input()

count = {}

for char in str:
    count[char] = count.get(char, 0) + 1


for k,v in count.items():
    print(k, ":", v)