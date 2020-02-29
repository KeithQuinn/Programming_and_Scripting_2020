student = {
    "name": input("Insert name: "),
    "modules": [
            {
            "subject" : input("Subject: "), 
            "grade": input("Grade: ")
            },
            {
            "subject" : input("Subject: "), 
            "grade": input("Grade: ")
             }   
            ]
}

print("Student: {}".format(student["name"]))

for module in student["modules"]:
    print("\t {} \t: {}".format(module["subject"], module["grade"]))