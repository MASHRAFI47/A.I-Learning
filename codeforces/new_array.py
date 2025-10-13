# https://codeforces.com/group/MWSDmqGsZm/contest/223205/problem/L

def concatArray (a, b):
    for element in b:
        print(element, end=" ")
        
    for element in a:
        print(element, end=" ")

inp = int(input())

array_A = input()
array_A_split = array_A.split()


array_B = input()
array_B_split = array_B.split()

concatArray(array_A_split, array_B_split)