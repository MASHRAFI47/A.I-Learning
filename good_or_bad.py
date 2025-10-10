# https://codeforces.com/group/MWSDmqGsZm/contest/219856/problem/H

inp = int(input())

for i in range(inp):
    goodBadString = input()
    if "010" in goodBadString:
        print("Good")
    elif "101" in goodBadString:
        print("Good")
    else:
        print("Bad")
