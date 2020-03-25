num = int (input("Please enter a positive integer: "))
div = 2

while num != 1:
    if (num % div) == 0:
        num = num / 2
        print(num)
    else:
        num = ((num * 3) + 1)
        print(num)





