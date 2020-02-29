from collections import Counter
from string import ascii_lowercase

path = "C:\\Users\\quinnk4\\Desktop\\Programming_and_Scripting_2020\\Trial and error files\\trialanderror.txt"

with open(path) as b:
        x = (Counter(letter for line in b
                    for letter in line.lower()
                    if letter == "e" in ascii_lowercase))

lettercount = Counter(x)

for letter in x:
    print(lettercount[letter])
