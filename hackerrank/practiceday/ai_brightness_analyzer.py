inp = input()
input = inp.split()

numbers = [int(num) for num in input]


sum = 0
for num in numbers:
    sum += num

avg_val = int(sum / len(numbers))

if avg_val < 85:
    print("Dark Image")
elif avg_val >= 85 and avg_val <= 170:
    print("Normal Image")
elif avg_val > 170:
    print("Bright Image")
