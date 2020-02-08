number = int (input("Please enter a positive integer: "))

p = number
m = 2

while p > 1:

    if (p % m) == 0:
    
     p = p / 2

     print(p)

    else:
    
        p = ((p * 3) + 1)

        print(p)





