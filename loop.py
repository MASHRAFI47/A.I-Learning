temp = [42, 39, 38, 28, 19]
for item in temp:
    print(item*(9/5)+32,"farenheit")

#short form
farenheit = [item*(9/5)+32 for item in temp]
print(farenheit)


far = [item*(9/5)+32 for item in temp if item%2 == 0]
print(far)


squares = [x**2 for x in range(1,6)]
print(squares)

unique_init = {item[0].lower() for item in ["Alice", "Bob", "Raian", "Rob"]}
print(unique_init)

nested_squares = [[x**2 for x in range(i, i+5) if x%2 == 0] for i in range(1, 10, 3)]
print(nested_squares)
 

number_descriptions = {
    num:("Even and divisible by 3" if num%2 == 0 and num%3 == 0
        else "even" if num%2 == 0
        else "odd and divisible by 3" if num % 3 == 0
        else "Odd")
    for num in range(1,11)
}
print(number_descriptions)