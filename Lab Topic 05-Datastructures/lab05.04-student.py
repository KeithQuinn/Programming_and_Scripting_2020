student = {
    "name":"Mary",
    "details": [
        {
            "courseName":"Programming",
            "grade":45
        },
        {
            "courseName":"History",
            "grade":99
        }
    ]
}

print("Student: {}".format(student["name"]))
for item in student["details"]:
    print("\t {} \t: {}".format(item["courseName"], item["grade"]))
