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
    
    transpose = []
    for i in range(len(matrix[0])):
        row = []
        for j in range(len(matrix)):
            row.append(matrix[j][i])
        transpose.append(row)
        
    for row in transpose:
        print(*row)






    