# Write a detailed pseudocode for a simple program that takes a number as input,
# calculates the square if it's even or the cube if it's odd, and then outputs the result.
# Incorporate conditional and looping constructs. 

num = int(input("Enter the number: "))
if num % 2==0:
    print("Square of the number is:", (num*num))
else:
    print("Cube of the number is:", (num*num*num))
        
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
factorial(5)
