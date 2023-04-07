from math import *

# take input from the user
a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))

# calculate the discriminant
d = b**2 - 4*a*c

# check if the roots are real or complex
if d < 0:
    print("Roots are complex")
else:
    # calculate the roots
    root1 = (-b + sqrt(d)) / (2*a)
    root2 = (-b - sqrt(d)) / (2*a)
    
    # print the roots
    print("Roots are:", root1, root2)
