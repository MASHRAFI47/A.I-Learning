t = int(input())

yes_count = 0
no_count = 0

for i in range(t):
    x = input()
    if x == "YES":
        yes_count += 1
    else:
        no_count += 1


if yes_count >= no_count:
    print("ACCEPT")
else:
    print("REJECT")