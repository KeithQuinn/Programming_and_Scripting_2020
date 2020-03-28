# user needs to input an a number to find the square root of, this is defined as variable sqrt_num.
sqrt_num = float (input("Enter a positive number: "))

# define fn(x) and fnprime(x)
def fn (x):
    return ((x * x) - sqrt_num)
def fnPrime (x):
    return (2 * x)

# initial guess required to start the iterative process
guess = 1

# the code uses a for loop with a range of 1 to 99 iterations
# however there is an if statement that breaks the for loop 
# if the difference between the current and next guess is less than 0.000001
for val in range (1, 100):
    nextguess = guess - fn(guess)/fnPrime(guess)
    if abs(nextguess - guess) < 0.000001: break
    guess = nextguess
    print(nextguess)