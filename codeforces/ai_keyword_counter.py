# better approach was making an array where you save the words and loop through them to count += 1

inp = input()

split_inp = inp.split()

count = 0

if "ai" in split_inp: 
    count += 1
if "data" in split_inp:
    count += 1
if "model" in split_inp:
    count += 1
if "learn" in split_inp:
    count += 1
if "train" in split_inp:
    count += 1
if "neural" in split_inp:
    count += 1


if count >= 2:
    print("AI Detected")
else:
    print("Not AI Related")
