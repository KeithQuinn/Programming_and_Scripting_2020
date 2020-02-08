# This program calculates how many tiles you will need
# when tiling a wall or floor (in m2).


length = float (input("Enter room length: "))

width = float (input("Enter room width: "))

area = length * width

needed = area * 1.05

print("You need", needed, "tiles in m2")