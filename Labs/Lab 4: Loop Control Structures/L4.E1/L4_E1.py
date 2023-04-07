while True:  # loop until a negative integer is given

    num = int(input())
    
    if num < 0:
        break  # terminate the loop if a negative integer is given
    
    elif num == 1:
        print("non-prime")  # 1 is not considered a prime number
        
    else:
        prime = True  # assume the number is prime
        
        for i in range(2, num):
            
            if num % i == 0:
                prime = False  # if the number is divisible by any other number than 1 and itself, it's not prime
                break  # exit the loop if the number is not prime
            
        if prime:
            print("prime")  # if the number is not divisible by any number other than 1 and itself, it's prime
            
        else:
            print("non-prime")  # if the number is divisible by any number other than 1 and itself, it's not prime
