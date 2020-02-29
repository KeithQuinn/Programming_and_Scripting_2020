import os.path
filename = "cont.txt"
if not os.path.isfile(filename):
    print("File doesn't exist")
    #writenumber(0)
else:
        print("File exists")

def readnumber ():
    try:
        with open (filename) as f:
            number = int(f.read())
            return number
    except IOError:
        return 0
  
