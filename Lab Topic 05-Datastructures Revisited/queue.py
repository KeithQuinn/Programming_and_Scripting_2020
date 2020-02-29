import random
queue = []
numberofnumbers = 10
rangeto = 100

for n in range(0,numberofnumbers):
    queue.append(random.randint(0,rangeto))

print("queue is {}".format(queue))

while len(queue) != 0:
    currentnumber = queue.pop(0)
    print ("current number is {} and the queue is {}".format(currentnumber, queue))

print("The queue is now empty")