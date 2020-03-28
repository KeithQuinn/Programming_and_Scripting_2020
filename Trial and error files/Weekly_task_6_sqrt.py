i = float (input("Enter a positive number: "))

def fn (x):
    return ((x * x) - i)

def fnPrime (x):
    return (2 * x)

x = 1

for val in range(10):
    nextx = x - ((fn(x)) / (fnPrime(x)))
    print(nextx)
    #x = nextx
print("The square root of", i, "is approx.",(round(x,1)))
