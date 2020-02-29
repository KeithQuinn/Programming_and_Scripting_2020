from collections import Counter
from string import ascii_lowercase

with open("Weekly_task_7_countes.txt") as b:
        x = (Counter(letter for line in b
                    for letter in line.lower()
                    if letter == "e" in ascii_lowercase))

lettercount = Counter(x)

for letter in x:
    print(lettercount[letter])
