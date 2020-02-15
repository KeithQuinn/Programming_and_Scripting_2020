#Keith Quinn
#Computing the primes.

#My list of primes = TBD


P = []

# Loop through all of the numbers we're checking for primality

for i in range(2, 100):
    isprime = True
    #loop through all values up to but not including i
    for j in range(2, i):
        #see if j divides i
        if i % j == 0:
            #if it does, i isn't prime so exit the loop and indicate it's not prime
            isprime = False
            break
        # If i is prime, then append to P.
    if isprime:
       P.append(i)

print(P)            

