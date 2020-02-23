students = []


def displayMenu ():
    print("What would you like to do?")
    print("\t(a) Add new student")
    print("\t(v) View students")
    print("\t(q) Quit")
    choice = input("Type one letter (a/v/q):").strip()
    return choice

def readModules():
    modules = []
    moduleName = input("\tEnter the first Module name (blank to end): ").strip()

    while moduleName != "":
        module = {}
        module["name"] = moduleName
        module["grade"] = int(input("\t\tEnter grade: "))
        modules.append(module)

        moduleName = input("\tEnter next module name (blank to end): ").strip()

    return modules

def doAdd():
    currentStudent = {}
    currentStudent ["name"] = input("Enter name: ")
    currentStudent ["modules"] = readModules()
    students.append(currentStudent)


def displayModules(modules):
    print("\t\t name\tgrade")
    for module in modules:
        print("\t\t{}\t{}".format(module["Name"], module["Grade"]))

def doView():
    print("all students")
    for student in students:
        print("\t{}".format(student["name"]))
        displayModules(student["modules"])

choice = displayMenu()

while (choice != "q"):
    if choice == "a":
        doAdd()
    elif choice == "v":
        doView()
    elif choice != "q":
        print("\nplease select either a,v or q")
    choice = displayMenu()

students = []



#print("you chose {}".format(choice))