#Write a program to show the example of following.

#1.      Function without Parameters:
#Code:
def greet():
    print("Hello, World!")

# Example usage:
greet()

#Output:
#Hello, World!

#2.      Function with Parameter:
#Code:
def greet(name):
    print("Hello, " + name + "!")

# Example usage:
greet("Vandana")

#Output:
#Hello, Vandana!

#3.      Function with Default Parameter:
#Code:
def greet(name="Stranger"):
    print("Hello, " + name + "!")

# Example usage:
greet()
greet("Maharashtra")

#Output:
#Hello, Stranger!
#Hello, Maharashtra!

#4.      Function with Return Keyword:
#Code:
def add(a, b):
    return a + b

# Example usage:
result = add(5, 3)
print("The sum is", result)

#Output:
#The sum is 8

#5.      Recursion:

#a) WAP to print factorial value of a given number using recursion.
#Code:
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Example usage:
num = int(input("Enter a number to find its factorial: "))
print("The factorial of", num, "is", factorial(num))

#Output:
#Enter a number to find its factorial: 8
#The factorial of 8 is 40320

#b) WAP to display Fibonacci series up to 10 iteration using recursion.
#Code:
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Example usage:
num_terms = 10
print("Fibonacci series up to", num_terms, "terms:")
for i in range(num_terms):
    print(fibonacci(i), end=" ")

#Output:
#Fibonacci series up to 10 terms:
#0 1 1 2 3 5 8 13 21 34 