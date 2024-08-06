#Q.1 print helloworld
#Code:
print("helloworld")

#Output:
#helloworld

#Q.2 describe local variable and global variable code
#Code:
# Global variable
x = "global"

def my_function():
    # Local variable
    x = "local"
    print("Inside the function, x is:", x)

my_function()
print("Outside the function, x is:", x)

#Output:
#Inside the function, x is: local
#Outside the function, x is: global

#Explanation:
#x = "global" defines a global variable.
#Inside my_function, x = "local" defines a local variable with the same name.
#Inside the function, the local variable x is used.
#Outside the function, the global variable x is used.

#Q.3 Write a code that describe Indentation error
#Code:
def my_function():
print(100)

Expected Error:
IndentationError: expected an indented block

Explanation: 
->The print statement inside my_function is not indented correctly. 
->In Python, code inside a function should be indented.

Correct Code:
def my_function():
    print(100)

#Output:
#100


#Q.4 write a code that describe local and global variable with same name
#Code:
# Global variable
x = 30

def my_function():
    # Local variable with the same name
    x = 40
    print("Inside the function, x is:", x)

my_function()
print("Outside the function, x is:", x)

#Output:
#Inside the function, x is: 40
#Outside the function, x is: 30

#Explanation:
#x = 30 is a global variable.
#Inside my_function, x = 40 creates a local variable with the same name.
#The function prints the local variable x which is 40.
#Outside the function, it prints the global variable x which is 30.

#Q.5 Write a code for string, int and float input.

#Code:
# String input (name)
name = input("Enter your name: ")

# Integer input (age)
age = int(input("Enter your age: "))

# Float input (height)
height = float(input("Enter your height: "))

print("Name:", name)
print("Age:", age)
print("Height:", height)

#My input:
#Enter your name: Vandana
#Enter your age: 22
#Enter your height: 5.2

#Output:
#Name: Vandana
#Age: 22
#Height: 5.2
