n = int(input())

target = float(input())

sum = 0.00

for i in range(n):
    x = float(input())
    sum += x

avg_val = sum / n

if avg_val <= target:
    print("PASS")
else:
    print("RETRY")