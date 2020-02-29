from collections import Counter
from string import ascii_lowercase


with open("trialanderror.txt") as b:
        x = (Counter(letter for line in b
                    for letter in line.lower()
                    if letter == "e" in ascii_lowercase))

lettercount = Counter(x)

for letter in x:
    print(lettercount[letter])









    #def count_letters(word, char):
      #  count = 0
       # for a in word:
        #        if char == a:
         #           count += 1
        #return count



#print(count_letters("trialanderrrror.txt", "r"))