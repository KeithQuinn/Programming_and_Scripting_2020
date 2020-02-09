# create a dictionary

currentbook = {
    "title" : "Harry Potter eats his dinner",
    "author" : "Just Kidding Rowling",
    "price" : 12
}

#print dictionary object
print(currentbook)

#print just the author
print(currentbook["author"])

#set attribute ISBN
currentbook["ISBN"] = "123455"

print(currentbook)

print ("The current book has these values:")
for value in currentbook.values():
    print("=> {}".format (value))