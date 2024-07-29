# <!-- 1. **Variables**:
#    Create a variable `num` and assign it the value `5`. -->
num = 5
print(num)


print("----------------------------------------------------------------------------------------------")

# <!-- 2. **Expressions**:
#    Write an expression to calculate the result of `3 + 4 * 2`.
   
result = 3 + 4 * 2
print(result)


print("----------------------------------------------------------------------------------------------")


# 3. **Statements**:
#    Write a statement to print the string `"Hello, World!"`.

print("Hello, World!")

print("----------------------------------------------------------------------------------------------")

# 4. **Variables**:
#    Create two variables `a` and `b` with values `10` and `20` respectively. Swap their values without using a temporary variable.

a = 10
b = 20
   
#Values after Swapping
a,b=b,a
print("The value of A is:",a)
print("The value of B is:",b)


print("----------------------------------------------------------------------------------------------")


# 5. **Expressions**:
#    Write an expression to calculate the area of a rectangle with length `l` and width `w`.
  
l = int(input("Enter the Length of the rectangle"))
w = int(input("Enter the Width of the rectangle"))
print("The area of the rectangle is:",(l*w))

print("----------------------------------------------------------------------------------------------")

# 6. **Statements**:
#    Write a statement to print all numbers from `1` to `10`.

for i in range(1,11):
    print(i)
    
    
print("----------------------------------------------------------------------------------------------")

# 7. **Variables**:
#    Create a variable `name` and assign it a string value.
name = "Satyam Singh"
print(name)


print("----------------------------------------------------------------------------------------------")

# 8. **Expressions**:
#    Write an expression to convert temperature from Fahrenheit to Celsius.

fahrenheit = float(input("Enter the Temperature in Fahrenheit: "))
celsius = (fahrenheit - 32) / (5/9)
print("Temperature in Celsius:", celsius)

print("----------------------------------------------------------------------------------------------")
 



# 9. **Statements**:
#    Write a statement to print the square of a number `x`.
x = int(input("Enter the value of x"))
print("The square of the number `x` is",(x*x))

print("----------------------------------------------------------------------------------------------")


#    10  Write an expression to concatenate two strings `s1` and `s2`.

s1 = "Satyam"
s2 = "Singh"

print(s1+s2)


# 11. **Variables**:
#     Create a variable `numbers` and assign it a list of numbers `[1, 2, 3, 4, 5]`.

list1 = [1, 2, 3, 4, 5]

print("----------------------------------------------------------------------------------------------")

# 12. **Expressions**:
#     Write an expression to calculate the square root of a number `x`.

number = float(input("Enter a number: "))
square_root = number ** 0.5
print("Square root of", number, "is", square_root)

print("----------------------------------------------------------------------------------------------")

# 13. **Expressions**:
#    Write an expression to calculate the average of three numbers `x`, `y`, and `z`.
x = int(input("Enter the Value of X"))
y = int(input("Enter the Value of Y"))
z = int(input("Enter the Value of Z"))
avg = (x+y+z) / 3
print("The Average of the three numbers are: ", avg)

print("----------------------------------------------------------------------------------------------")


# 14. **Expressions**:
#    Write an expression to calculate the area of a circle with radius `r`.
pi = 3.14
r = int(input("Enter the radius of the circle"))
print("The area of the circle is: ", (pi*r*r))

print("----------------------------------------------------------------------------------------------")

# 15. **Expressions**:
#     Write an expression to check if a year `year` is a leap year. -->

year = int(input("Enter the Year"))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("It's a Leap Year")
else:
    print("Not Leap Year")
    
    
# str = input("Enter the String: ")
# element = input("Enter the element count: ")

# count = 0

# for char in str:
#     if char == element:
#         count += 1
        
# print("The element '{}' apperas '{}' times in the string.".format(element,count))

# Wap to take a lower case input and convert the entire screen into Captalize. without using Captalize method
# str = input("Enter the string in lower case: ")
# str[0].upper

# str = input("Enter the string in the lower case: ")

# if str.islower():
#     print("True")
# else:
#     print("False")
    
# str = input("Enter the string in the lower case: ")
# result =""

# for char in str:
#     if ord('a') <= ord(char) <= ord('z'):
#         result += chr(ord(char)-32)
#     else:
#         result += char
# print(result)

# str = input("ENTER THE STRING: ")
# if str[0].isupper() and str[1:].islower:
#     print("True")
# else:
#     print("False")




# l = [1, 2, 3, 4, 4, 5, 6, 7, 8, 10, 111]
# rmv = int(input("Enter the number to be removed from the list: "))

# while rmv in l:
#     l.remove(rmv)

# print("List after removal:", l)


# l = ['Naman Bansal', 'Aarti Sharma', 'Mayank Agrawal', 'Shahrukh Khan']
# new_list = []

# for name in l:
#     initials = ""
#     parts = name.split() 
#     for part in parts:
#         initials += part[0]  
#     new_list.append(initials)

# print(new_list)


# list = ['Naman Bansal', 'Aarti Sharma', 'Mayank Agrawal', 'Shahrukh Khan']
# l1 = []
# l2 = []

# for name in list:
#     ns = name.split()
#     print(ns)
#     l1.append(ns[0])
#     l2.append(ns[-1])
# print(l1)
# print(l2)

# l1 = ['Naman', 'Aarti', 'Mayank', 'Shahrukh']
# l2 = ['Bansal', 'Sharma', 'Agrawal', 'Khan']

# l3 = []
# for firstname in l1:
#     for lastname in l2:
#         l3.append(firstname + ' ' + lastname)
#         break  
# print(l3)

# list = ['Naman Bansal', 'Aarti Sharma', 'Mayank Agrawal', 'Shahrukh Khan']
# vowels = 'aeiouAEIOU'

# for name in list:
#     count = 0
#     for char in name:
#         if char in vowels:
#             count += 1
#     print("Number of vowels in '{}': {}".format(name, count))

            
# list = ['Naman Bansal', 'Aarti Sharma', 'Mayank Agrawal', 'Shahrukh Khan']
# l1 = []
# for name in list:
#     ns = name.split()
#     # print(ns)
#     l1.append(ns[0][0] + '. ' + ns[1])
# print(l1)
    

list = ['Naman Bansal', 'Aarti Sharma', 'Mayank Agrawal', 'Shahrukh Khan']
l1 = []

for firstname in list:
    ns = firstname.split()
    first_name=  ns[0]
    last_name = (ns[-1])
    l1.append((last_name + " " + first_name))
print(l1)

list = ['Naman kumar Bansal', 'Aarti Sharma', 'Mayank Agrawal', 'Shahrukh Khan']
l1 = []
rev_list = list.reverse()
for name in list:
    ns = name.split()
    print(ns)
    first_name = ' '.join(ns[:-1])
    last_name = (ns[-1])
    l1.append((last_name + " " + first_name))
print(l1)