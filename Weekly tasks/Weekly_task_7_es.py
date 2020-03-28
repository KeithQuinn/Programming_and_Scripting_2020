# open txt file as doc, lower case all letters and count the number of e's.

with open("Weekly_task_7_countes.txt") as doc:
    for line in doc:
       line = line.lower()
print(line.count("e"))