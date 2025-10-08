inp = input()

numbers = inp.split()

first_number = int(numbers[0])
second_number = int(numbers[1])

last_digit_of_x = first_number%10
last_digit_of_y = second_number%10

sum_of_last_digits = last_digit_of_x + last_digit_of_y
print(sum_of_last_digits)