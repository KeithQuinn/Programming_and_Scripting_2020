import random

howmany    = 10
tophowmany = 3
rangeFrom  = 0
rangeto    = 100

numbers = []

for i in range(0, howmany):

    numbers.append(random.randint(rangeFrom,rangeto))

print ("{} random numbers\t {}".format(howmany, numbers))

topones = numbers.copy()
topones.sort(reverse = True)
print ("The top {} are \t\t {}".format(tophowmany, topones[0:tophowmany]))