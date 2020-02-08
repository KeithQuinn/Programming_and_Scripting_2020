# Keith Quinn
# Check if a number is prime
# The primes are 2, 3, 5, 7, 11, 13

p = 221
isprime = True

for m in range(2, p-1):
    if p % m == 0:
        isprime = False

if isprime:
    print(p, "is a prime number")
else:
    print (p, "isn't a prime number")  

print("Thanks for running my program")