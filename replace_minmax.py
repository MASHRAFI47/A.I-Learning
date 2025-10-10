### https://codeforces.com/group/MWSDmqGsZm/contest/219774/problem/M

#l = list(map(int, input().split()))

t = int(input())

inp = input()

input = inp.split()

numbers = [int(num) for num in input]

highest_number_in_list = max(numbers)
lowest_number_in_list = min(numbers)

temp_highest_index = numbers.index(highest_number_in_list)
temp_lowest_index = numbers.index(lowest_number_in_list)

numbers[temp_highest_index] = lowest_number_in_list
numbers[temp_lowest_index] = highest_number_in_list


for num in numbers:
    print(num, end=" ")


