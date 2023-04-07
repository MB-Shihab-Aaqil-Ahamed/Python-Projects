# Abundant Numbers

## Description
In number theory, an abundant number is a number for which the sum of its proper divisors is greater than the number itself. 

This program takes input a positive integer `n` greater than 1 and outputs the number of abundant numbers from 2 to n inclusive. It outputs 'Invalid Input' for inputs less than 2.

## Instructions

1. Enter a positive integer `n` greater than 1.
2. The program will output the number of abundant numbers from 2 to n inclusive.
3. If the input number is less than or equal to 1, the program will output "Invalid Input".
4. 
## Example

Input: 15

Output: Number of abundant numbers from 1 to 15 is 1

## Code Explanation

- The user is asked to enter a positive integer greater than 1.
- An empty list is initialized to store abundant numbers.
- The code then checks if the input number is greater than 1.
- If it is, the code loops through all numbers from 2 to n.
- For each number, the code loops through all numbers from 1 to x-1 to check if they are proper divisors of x.
- The sum of proper divisors is calculated and compared with x to determine if x is abundant.
- If x is abundant, it is added to the list of abundant numbers.
- The number of abundant numbers in the list is printed.
- If the input number is less than or equal to 1, the code prints "Invalid Input".

## Code
```python
# Take input from user
n = int(input("Input number: "))

# Initialize an empty list to store abundant numbers
abundant_numbers = []

# Check if the input number is greater than 1
if n > 1:

    # Loop through all numbers from 2 to n
    for x in range(2, n+1):

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
    print("Number of abundant numbers from 1 to", n, "is", len(abundant_numbers))

# If the input number is less than or equal to 1, print "Invalid Input"
else:
    print("Invalid Input")
```
