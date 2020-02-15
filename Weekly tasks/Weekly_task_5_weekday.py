day = input("Enter day: ")

weekday = ["Monday", "monday", "Tuesday", "tuesday", "Wednesday", "wednesday", "Thursday", "thursday", "Friday", "friday"]

weekend = ["Saturday", "saturday", "Sunday", "sunday"]

if day in weekday:
    print("Yes, unfortunately today is a weekday.")
else:
    if day in weekend:
            print("It is the weekend, yay!")
    else:
        print("***error***")