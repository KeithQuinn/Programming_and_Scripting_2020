#program will strip any leading or trailing spaces, and will also convert the string to lowercase

string = input("please enter a string: ")

normalised = string.strip().lower()

stringlength = len(string)
normalisedlength = len(normalised)

print("Normalised string is:  {}". format (normalised))
print("The original string is {}". format (stringlength))
print("The normalised string is {}". format (normalisedlength))
print("The string has been reduced from {} to {}". format (stringlength, normalisedlength))