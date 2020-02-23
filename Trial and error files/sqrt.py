i = float (input("Enter number: "))

def fn (x):
    return ((x * x) - i)

def fnPrime (x):
    return (2 * x)

x = 1


x2 = x - ((fn(x)) / (fnPrime(x)))

print(x2)

x3 = x2- ((fn(x2)) / (fnPrime(x2)))

print(x3)

x4 = x3- ((fn(x3)) / (fnPrime(x3)))

print(x4)