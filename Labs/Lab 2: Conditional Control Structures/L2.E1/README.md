# Triangle Type Detector

This program takes three angles of a triangle as input and outputs the type of the triangle.

## Usage

Run the program and enter the three angles of the triangle when prompted. The program will then determine if the angles form a triangle or not, and if so, what type of triangle it is.

### Example

Input:

Enter angle 1: 10
Enter angle 2: 15
Enter angle 3: 20

Output:

Acute angled triangle


## Implementation

The program uses the following logic to determine the type of triangle:

1. Check if any angle is zero or if the angles do not form a triangle.
2. Check if the sum of the angles is 180 degrees (i.e. if they form a triangle).
3. If they form a triangle, determine the type of the triangle based on the size of its angles.

### Triangle Types

The program can detect the following types of triangles:

- Right angled triangle: One of the angles is exactly 90 degrees.
- Obtuse angled triangle: One of the angles is greater than 90 degrees.
- Acute angled triangle: All of the angles are less than 90 degrees.


## License

This program is licensed under the MIT License. See `LICENSE` for more information.
