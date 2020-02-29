students = []

def displaymenu():
    print("What would you like to do?")
    print("\t (a) Add new student")
    print("\t (v) View students")
    print("\t (q) Quit")
    choice = input("Type one letter (a/v/q) :").strip()
    return choice

def readmodules():
    modules = []
    modulename = input("\tEnter the first module name (blank to quit): ").strip()
    while modulename != "":
        module = {}
        module["name"] = modulename
        module["grade"] = int (input("\t\tEnter grade: "))
        modules.append(module)
        modulename = input("\tEnter next module name (blank to quit): ").strip()
    return modules

def doAdd():
    currentstudent = {}
    currentstudent["name"] = input("Enter name: ")
    currentstudent["modules"] = readmodules()
    students.append(currentstudent)

def doView():
    for currentstudent in students:
        print("\t{}".format(currentstudent["name"]))
        displaymodules(currentstudent["modules"])

def displaymodules (modules):
    print ("\tName \tGrade")
    for module in modules:
        print("\t{} \t{}".format(module["name"], module["grade"]))

choice = displaymenu()

while choice !="q":
    if choice == "a":
        doAdd()
    elif choice =="v":
        doView()
    elif choice !="q":
        print("Please enter a, v or q")
    choice = displaymenu()
    