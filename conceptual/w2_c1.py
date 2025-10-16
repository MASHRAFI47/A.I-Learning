from functools import reduce

from pathlib import Path
import csv

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
squared = [n*n if(n*n) > 30 else n for n in numbers if n%2 == 1]
print(squared) #[1, 3, 5, 49, 81]


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
f = [j for i in matrix for j in i]
print(f) #[1, 2, 3, 4, 5, 6, 7, 8, 9]



##CSV DATA CLEANING
raw_data = [' 25 ', '30 ', ' 42', 'abc', '50']
clean = [int(r.strip()) for r in raw_data if r.strip().isdigit()] 
print(clean) #[25, 30, 42, 50]


def greet():
    print("Hello")

greet2 = lambda : print("Hello")
print(greet2())

greet3 = lambda name : print("Hello", name)
greet3("Rakib")



### VALID EMAIL FILTER
emails = ["rakib@gmail.com", "invalid", "test@gmail.com", "no@", "admin@site"]
selected = list(filter(lambda e : '@' in e and '.' in e, emails))
print(selected)



### Count VOWELS PRINTING
sentences = ["I love Python", "Machine Learning is fun", "AI is the future"]

def count_vowels(text):
    s = 0
    for ch in text.lower():
        if ch in 'aeiou':
            s+=1

    return s

total = reduce(lambda x,y : x + count_vowels(y), sentences, 0)
print(total) #19




### WRITE AND READ CSV FILE
Data_Path = Path('data')
Data_Path.mkdir(exist_ok=True)
csv_path = Data_Path / "student.csv"
#print(csv_path) #data\student.csv

#write
with csv_path.open('w', newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Age"])
    writer.writerow(["Mashrafi", 23])
    writer.writerow(["Rakib", 17])

#read
with csv_path.open("r", encoding="utf-8") as file:
    reader = csv.reader(file)
    read_list = list(reader)
    print(read_list) #[['Name', 'Age'], ['Mashrafi', '23'], ['Rakib', '17']]