#include <stdio.h>
#include <math.h>

int main() {
    int a, b, c;
    double disc, root1, root2;

    // take input from the user
    printf("Enter a: Enter b: Enter c: ");
    scanf("%d %d %d", &a, &b, &c);

    // calculate the discriminant
    disc = b * b - 4 * a * c;

    // check if the roots are real or complex
    if (disc < 0) {
        printf("Roots are imaginary\n");
    }
    else {
        // calculate the roots
        root1 = (-b + sqrt(disc)) / (2.0 * a);
        root2 = (-b - sqrt(disc)) / (2.0 * a);
        
        // print the roots
        printf("Roots are: %.1lf %.1lf\n", root1, root2);
    }

    return 0;
}

