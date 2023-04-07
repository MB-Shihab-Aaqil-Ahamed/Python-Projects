## Program to Transpose a Matrix

This program reads a matrix with any dimension from the keyboard until -1 is entered and outputs its transpose. It uses a 2D (two-dimensional) list to store the matrix.

The program handles exceptions such as checking the invalid rows with an inconsistent number of elements. It prints Invalid Matrix as the error message for invalid rows and breaks out of the program. If any other exceptions are caught, it prints Error and exits the program.

Here is the Python code for the program:
```python
# create an empty 2D list to store the matrix
matrix = []

# read the matrix from the keyboard until -1 is entered
while True:
    row = input().split()
    if row == ['-1']:
        break
    try:
        row = [int(x) for x in row]
        matrix.append(row)
    except ValueError:
        print("Invalid Matrix")
        matrix = []
        break

# check if the matrix is valid
valid = True
for row in matrix:
    if len(row) != len(matrix[0]):
        valid = False
        print("Invalid Matrix")
        break

# if the matrix is valid, compute and print the transpose
if valid:
    try:
        transpose = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
        for row in transpose:
            print(*row)
    except:
        print("Error")
```
  
To use this program, simply run it in a Python environment, and enter the matrix elements row by row. Separate the elements in each row with spaces, and enter -1 on a separate line to stop entering the matrix.

## License

This program is licensed under the MIT License. See the `LICENSE` file for details.





