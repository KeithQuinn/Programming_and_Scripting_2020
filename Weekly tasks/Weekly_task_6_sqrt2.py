i = float (input("Enter a positive number: "))

def fn (x):
    return ((x * x) - i)

def fnPrime (x):
    return (2 * x)

x = 1
   
for val in range(10):
    nextx = x - ((fn(x)) / (fnPrime(x)))
    while (nextx/x) > 0.5:
    x = nextx
    print(nextx)
