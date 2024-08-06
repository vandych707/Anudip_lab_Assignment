#1.Write a Python program that takes a number as input and prints "Even" if the number is even and "Odd" if it's odd.
#Code:
def check_even_odd(number):
    if number % 2 == 0:
        print("Even")
    else:
        print("Odd")

# Example usage:
num = int(input("Enter a number: "))
check_even_odd(num)

#Output:
#Enter a number: 9
#Odd


#2.Create a Python program that checks whether a person is eligible to vote (18 years or older) based on their age.
#Code:
def check_voting_eligibility(age):
    if age >= 18:
        print("Eligible to vote")
    else:
        print("Not eligible to vote")

# Example usage:
age = int(input("Enter your age: "))
check_voting_eligibility(age)

#Output:
#Enter your age: 19
#Eligible to vote

#3.Write a Python program that determines if a given year is a leap year or not.
#code:
def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print("Leap year")
    else:
        print("Not a leap year")

# Example usage:
year = int(input("Enter a year: "))
is_leap_year(year)

#Output:
#Enter a year: 2024
#Leap year



#4.Create a Python program that checks if a user-given number is positive, negative, or zero.
#Code:
def check_number_sign(number):
    if number > 0:
        print("Positive")
    elif number < 0:
        print("Negative")
    else:
        print("Zero")

# Example usage:
num = float(input("Enter a number: "))
check_number_sign(num)

#Output:
#Enter a number: -9
#Negative

#5.Write a Python program that determines the largest of three numbers entered by the user.

#Code:
def largest_of_three(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

# Example usage:
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

largest = largest_of_three(num1, num2, num3)
print("The largest of the three numbers is", largest)

#Output:
#Enter the first number: 8
#Enter the second number: 15
#Enter the third number: 9
#The largest of the three numbers is 15.0
