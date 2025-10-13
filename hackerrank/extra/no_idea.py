# # https://www.hackerrank.com/challenges/no-idea/problem

inp = input()
constraints = inp.split()
con_nums = [int(x) for x in constraints]


arr = input()
arr_split = arr.split()
int_arr = [int(x) for x in arr_split]


set_a = set()
set_b = set()


set_a_input = input()
set_a_input_split = set_a_input.split()
set_a_nums = [int(x) for x in set_a_input_split]

for element in set_a_nums:
    set_a.add(element)


set_b_input = input()
set_b_input_split = set_b_input.split()
set_b_nums = [int(x) for x in set_b_input_split]

for element in set_b_nums:
    set_b.add(element)


happiness = 0

for element in int_arr:
    if element in set_a:
        happiness += 1
    if element in set_b:
        happiness -= 1

print(happiness)