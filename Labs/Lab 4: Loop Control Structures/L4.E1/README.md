## Exercise L4.E1

Develop a program that takes as input a series of positive integers and outputs whether each is a prime. The program should terminate if a negative integer is given as the input. 

A prime number is a number that is divisible by only 1 and itself. However 1 is not considered a prime number. 

Execution of your program should produce something similar to the following:

|Input    | Result     |
|---------|------------|
|2        | prime      |
|1        | non-prime  |
|3        | prime      |
|10       | non-prime  |
|11       | prime      |
|30       | non-prime  |
|82589933 | prime      |
|-1|


The solution code in Python is:

```python
while True:
    num = int(input("Enter a positive integer (enter a negative integer to terminate): "))
    if num < 0:
        break
    elif num == 1:
        print("non-prime")
    else:
        prime = True
        for i in range(2, num):
            if num % i == 0:
                prime = False
                break
        if prime:
            print("prime")
        else:
            print("non-prime")
```

In the above code, we take the input from the user in a loop until the user enters a negative integer. If the user enters a negative integer, we break out of the loop. If the user enters 1, we print "non-prime" since 1 is not considered a prime number. If the user enters any other positive integer, we use a loop to check if it is a prime number. If it is a prime number, we print "prime", otherwise we print "non-prime".
