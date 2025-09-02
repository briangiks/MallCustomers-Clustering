#Importing the necessaries math
import math

#Asking the user to enter the radius of a sphere
radius = float(input("Enter the radius of the sphere:"))

#Formula for volume of a sphere
volume = (4/3) * math.pi * (radius**3)

#Output the volume of the sphere
print("The volume of the sphere is: %.2f" %volume)
