# Take input from user for the message and the base
message = input("Enter message: ")
base = int(input("Enter base: "))

# Initialize an empty string to store the encrypted message
encrypted_message = ""

# Loop through each character in the message
for c in message:

    # Get the ASCII value of the character
    ascii_value = ord(c)

    # Convert the ASCII value to the given base
    base_value = ""
    while ascii_value > 0:
        remainder = ascii_value % base
        base_value = str(remainder) + base_value
        ascii_value = ascii_value // base

    # Concatenate the base value to the encrypted message
    encrypted_message += base_value

# Print the encrypted message
print(encrypted_message)

    