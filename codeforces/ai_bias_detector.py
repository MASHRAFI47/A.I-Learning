inp = input()

letters = inp.split()

A_count = letters.count('A')
B_count = letters.count('B')

A_percentage = (A_count / len(letters)) * 100
B_percentage = (B_count / len(letters)) * 100

if A_percentage > 70 or B_percentage > 70:
    print("Biased Model")
else:
    print("Fair Model")