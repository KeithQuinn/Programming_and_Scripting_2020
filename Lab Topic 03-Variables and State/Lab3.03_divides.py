# Program divides the first number by the second number

a = int (input("Enter first number: "))
b = int (input("Enter second number: "))

answer = a // b

remainder = a % b

print(a, "divided by", b, "is", answer, "with a remainder of", remainder)

print("{} divided by {} is {} with a remainder of {}" .format (a, b, answer, remainder))