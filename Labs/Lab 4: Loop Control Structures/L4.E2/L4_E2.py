# Take input from user
num = int(input("Input number: "))

# Initialize an empty list to store abundant numbers
abundant_numbers = []

# Check if the input number is greater than 1
if num > 1:

    # Loop through all numbers from 2 to n
    for x in range(2, num + 1):

        # Initialize sum of proper divisors to 0
        divisors_sum = 0

        # Loop through all numbers from 1 to x-1
        for i in range(1, x):

            # Check if i is a proper divisor of x
            if x % i == 0:

                # Add i to the sum of proper divisors
                divisors_sum += i

        # Check if the sum of proper divisors is greater than x
        # and x is not already in the list of abundant numbers
        if divisors_sum > x and x not in abundant_numbers:

            # Add x to the list of abundant numbers
            abundant_numbers.append(x)

    # Print the number of abundant numbers from 1 to n
    print("Number of abundant numbers from 1 to", num, "is", len(abundant_numbers))

# If the input number is less than or equal to 1, print "Invalid Input"
else:
    print("Invalid Input")
