# Prompt user to input monthly consumption
consumption = int(input())

# Initialize fixed charge and total bill amount
fixed_charge = 0
total_bill = 0

# Calculate bill amount based on monthly consumption
if consumption >= 0 and consumption <= 30:
    fixed_charge = 30
    total_bill = fixed_charge + consumption * 2.5
    
elif consumption >= 31 and consumption <= 60:
    fixed_charge = 60
    total_bill = fixed_charge + (30 * 2.5) + ((consumption - 30) * 4.85)
    
elif consumption >= 61 and consumption <= 90:
    fixed_charge = 90
    total_bill = fixed_charge + (60 * 7.85) + ((consumption - 60) * 10)
    
elif consumption >= 91 and consumption <= 120:
    fixed_charge = 480
    total_bill = fixed_charge + (60 * 7.85) + (30 * 10) + ((consumption - 90) * 27.75)
    
elif consumption >= 121 and consumption <= 180:
    fixed_charge = 480
    total_bill = fixed_charge + (60 * 7.85) + (30 * 10) + (30 * 27.75) + ((consumption - 120) * 32)
    
elif consumption > 180:
    fixed_charge = 540
    total_bill = fixed_charge + (60 * 7.85) + (30 * 10) + (30 * 27.75) + (60 * 32) + ((consumption - 180) * 45)
    
else:
    print("Invalid input. Please enter a non-negative integer value for monthly consumption.")

# Output the calculated electricity bill
if total_bill > 0:
    print(total_bill)
