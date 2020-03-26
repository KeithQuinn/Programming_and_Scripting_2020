import datetime

day = (datetime.datetime.today().weekday())
# Returns the day of the week as an integer, where Monday is 0 and Sunday is 6
# Days less than or equal to 4 cover Monday to Friday inclusive

if day <= 4:
    print("Got to work today, it's a weekday.")
else:
    print("Excellent, it's the weekend!")