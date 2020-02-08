#This program will calculate a persons BMI.
#This calculation is based of height and weight.

Weight = float (input("Enter Weight in kg: "))
Height = float(input("Enter Height in cm: "))

Heightcm2 = Height * Height

Heightm2 = Heightcm2 / 10000

BMI = Weight / Heightm2

print("Your BMI is", BMI,)