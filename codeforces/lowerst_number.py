t = int(input())
inp = input()
numbers = inp.split()

int_numbers = [int(num) for num in numbers]

sorted_numbers = [int(num) for num in numbers]
sorted_numbers.sort()

lowest_number = sorted_numbers[0]

index = 0
i = 1
for num in int_numbers:
    if num == lowest_number:
        index = i
        break
    else:
        i = i+1

print(lowest_number, index)