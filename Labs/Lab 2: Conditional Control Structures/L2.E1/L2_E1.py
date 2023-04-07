# program to check the type of triangle based on its angles

# Get the input angles from the user
angle1 = int(input("Enter angle 1: "))
angle2 = int(input("Enter angle 2: "))
angle3 = int(input("Enter angle 3: "))

# check if angles form a triangle
if angle1 == 0 or angle2 == 0 or angle3 == 0:  # Check if any angle is zero or if the angles form a triangle
    print("Angles do not form a triangle")

elif (angle1 + angle2 + angle3) != 180:  # Check if the sum of the angles is 180 degrees (i.e. if they form a triangle)
    print("Angles do not form a triangle")

else:  # If they form a triangle, determine the type of the triangle
    # check the type of triangle
    if angle1 == 90 or angle2 == 90 or angle3 == 90:  # if one angle is 90 degrees, it is a right angled triangle
        print("Right angled triangle")
        
    elif angle1 > 90 or angle2 > 90 or angle3 > 90:  # if one angle is greater than 90 degrees, it is an obtuse angled triangle
        print("Obtuse angled triangle")
    
    else:  # otherwise, it is an acute angled triangle
        print("Acute angled triangle")
