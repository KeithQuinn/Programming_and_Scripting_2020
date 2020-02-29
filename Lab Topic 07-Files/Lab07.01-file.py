filename = "count.txt"

def readnumber ():
    with open(filename) as f:
        number = int(f.read())
        return number

def writenumber (number):
    with open(filename, "wt") as f:
        f.write(str(number))
        return number

num = readnumber()
num += 1
print("We have run this program {} times".format(num))

writenumber(num)