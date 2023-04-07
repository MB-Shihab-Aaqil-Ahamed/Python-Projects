# Take 10 numbers as input from the user
numbers = input().split()


# Initialize an empty list to store the converted numbers
converted_numbers = []

# Loop through each element in the original list of numbers
for num in numbers:
    
    # Convert the string element to a float and append it to the new list
    converted_numbers.append(float(num))


# Find the minimum and maximum numbers using min() and max() functions
minimum = min(converted_numbers)
maximum = max(converted_numbers)

# Print the results
print("Minimum = ", minimum)
print("Maximum = ", maximum)

    