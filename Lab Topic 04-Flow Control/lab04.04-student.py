students = []

firstname = input("enter firstname (blank to quit): ").strip()

while firstname != "":
    student = {}
    student["firstname"] = firstname
    lastname = input("enter lastname: ").strip()
    student["lastname"] = lastname
    students.append(student)

    firstname = input("enter firstname of next (blank to quit): ").strip()

print("Here are the students you entered: ")
for currentstudents in students:
    print ("{} {}".format(currentstudents["firstname"], currentstudents["lastname"]))
