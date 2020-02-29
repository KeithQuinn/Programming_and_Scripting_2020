filename = "count.txt"

def writenumber (number):
    with open(filename, "wt") as f:
        f.write(str(number))
        return number

writenumber(6)