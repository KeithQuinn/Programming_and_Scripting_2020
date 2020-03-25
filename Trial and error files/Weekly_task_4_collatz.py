number = int (input("Please enter a positive integer: "))

p = number
m = 2

while p > 1:

    if (p % m) == 0:

     print(p, "is an even number and so it is divided by 2: ")
    
     p = p / 2

     print("the new value is",p)

    else:
        print(p, "is not an even number and so it is multiplied by 3 and 1 is added")
    
        p = ((p * 3) + 1)

        print("the new value is",p)





