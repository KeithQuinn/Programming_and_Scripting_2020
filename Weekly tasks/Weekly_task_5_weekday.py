day = input("Enter day: ").lower()

weekday = ["monday", "tuesday", "wednesday", "thursday", "friday"]

weekend = ["saturday", "sunday"]

if day in weekday:
    print("Yes, unfortunately today is a weekday.")
else:
    if day in weekend:
            print("It is the weekend, yay!")
    else:
        print("***error***")