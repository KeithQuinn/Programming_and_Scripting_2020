#Purpose of the program
#This program will calculate a persons BMI.

#Required inputs 
Weight = float (input("Enter Weight in kg: "))
Height = float(input("Enter Height in cm: "))

#Height calculation in m2
Heightcm2 = Height**2
Heightm2 = Heightcm2 / 10000

#BMI calculation and rounding
BMI = Weight / Heightm2
BMI2 = (round (BMI,2))

#Show result
print("Your BMI is", BMI2,)