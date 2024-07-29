# 1. Define a function called greet that takes a name as an argument and prints a greeting message. 
# Call the function with your name as the argument.

# def greet(name):
#     print("Hello,", name, "How are you?")
# greet("Vaish")

# 2. Define a function called check_even that takes a number as an argument and prints whether the number is even or odd.

# def check_even(num):
#     if num % 2 == 0:
#         print("Even Number")
#     else:
#         print("Odd Number")
# x = int(input("Enter the Value of X"))        
# check_even(x)


# 3. Define a function called 
# print_numbers that takes a number as an argument and prints all numbers from 1 to that number using a for loop.

# def print_numbers(num):
#     for i in range(1,num):
#         print(i)
        
# print_numbers(100)


# 4. Define a function called print_even that takes a number as 
# an argument and prints all even numbers from 1 to that number using a for loop and an if statement.

# def print_even(num):
#     for i in range(1,num +1):
#         if num % 2 == 0:
#             print(i)
# print_even(20)


def check_voting_eligibility(age, is_resident):
    if age>=18 and is_resident:
        return True
    else:
        return False
        
age = int(input("Ente the age :")) 
is_resident = input("Are you from india ? True or False:")
is_resident = bool(is_resident.lower() == 'true')

print(check_voting_eligibility(age, is_resident))
    