# https://codeforces.com/group/MWSDmqGsZm/contest/219774/problem/K

inp = int(input())

number = int(input())

sum = 0

while number > 0:
    last_digit = int(number % 10)
    sum += last_digit
    number /= 10

print(sum)