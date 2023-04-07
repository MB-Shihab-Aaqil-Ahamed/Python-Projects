## Encryption Program

This program encrypts a message using a given base. It works by obtaining the ASCII value of each character in the message and converting that number into the given base. Then, the converted values of all the characters are aggregated (concatenated) in the order they appear in the message, resulting in the encrypted message.

Input
message: a string representing the message to be encrypted.
base: an integer representing the base to be used for encryption.

Output
The encrypted message as a string.

Process
- For each character in the message, get its ASCII value using the ord() function.
- Convert the ASCII value to the given base using the built-in bin() function.
- Remove the prefix "0b" from the binary representation.
- Concatenate the binary representations of all the characters in the order they appear in the message.

Example 

Input:

Enter message: Welcome to CSE
Enter base: 4

Output:

Encoded message: 721011081081113211911111410810033
