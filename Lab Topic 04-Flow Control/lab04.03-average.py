numbers = []


number = float (input("Enter number (0 to quit): "))

while number != 0:
    numbers.append(number)

    number = float (input("Enter another number (0 to quit): "))

for value in numbers:
    print(value)

average = float(sum(numbers)) / len(numbers)

print("The average is {}".format(average))

