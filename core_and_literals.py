x = 42
y = 3.14
z = "hello"
t = True
lst = [1, 2, 3, ["Arif", "rahul"], 4]



tpl = (1, 2, 3)
dct = {
    "a": 1,
    "b": 2,
    "a": 3, #if there are duplicate values in dictionary, it will assign with the latest or last key value pair
}
st = {1, 2, 3 , 4}

print(lst)
print(type(x), type(y), type(z), type(t), type(lst), type(tpl), type(dct), type(st))

print(lst[0:2]) #[1, 2] middle slice
print(lst[-2:]) #last 2
print(lst[::2]) #step slice
print(lst[::-1]) #reverse print
print(lst[-5:-2])


