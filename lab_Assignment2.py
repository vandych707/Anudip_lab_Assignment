# Q.1 Write a program for arithmatic operators
# Code:
# Initial values
a = 15
b = 4

# Addition
addition = a + b
print("Addition (a + b):", addition)

# Subtraction
subtraction = a - b
print("Subtraction (a - b):", subtraction)

# Multiplication
multiplication = a * b
print("Multiplication (a * b):", multiplication)

# Division
division = a / b
print("Division (a / b):", division)

# Modulus
modulus = a % b
print("Modulus (a % b):", modulus)

# Exponentiation
exponentiation = a ** b
print("Exponentiation (a ** b):", exponentiation)

# Floor Division
floor_division = a // b
print("Floor Division (a // b):", floor_division)

# Output:
# Addition (a + b): 19
# Subtraction (a - b): 11
# Multiplication (a * b): 60
# Division (a / b): 3.75
# Modulus (a % b): 3
# Exponentiation (a ** b): 50625
# Floor Division (a // b): 3


# Q.2 Write a program for assignment operators
# Code:
# Initial value
x = 10
print("Initial value of x:", x)

# Addition assignment
x += 5  # equivalent to x = x + 5
print("After addition assignment (x += 5):", x)

# Subtraction assignment
x -= 3  # equivalent to x = x - 3
print("After subtraction assignment (x -= 3):", x)

# Multiplication assignment
x *= 2  # equivalent to x = x * 2
print("After multiplication assignment (x *= 2):", x)

# Division assignment
x /= 4  # equivalent to x = x / 4
print("After division assignment (x /= 4):", x)

# Modulus assignment
x %= 3  # equivalent to x = x % 3
print("After modulus assignment (x %= 3):", x)

# Exponentiation assignment
x **= 2  # equivalent to x = x ** 2
print("After exponentiation assignment (x **= 2):", x)

# Floor division assignment
x //= 2  # equivalent to x = x // 2
print("After floor division assignment (x //= 2):", x)

# Output:
# Initial value of x: 10
# After addition assignment (x += 5): 15
# After subtraction assignment (x -= 3): 12
# After multiplication assignment (x *= 2): 24
# After division assignment (x /= 4): 6.0
# After modulus assignment (x %= 3): 0.0
# After exponentiation assignment (x **= 2): 0.0
# After floor division assignment (x //= 2): 0.0

# Q.3Write a program for Bitwise operators 

# Code:
# Function to demonstrate bitwise operators
def bitwise_operators(a, b):
    # Bitwise AND
    and_result = a & b
    print(f"Bitwise AND of {a} & {b} = {and_result}")
    
    # Bitwise OR
    or_result = a | b
    print(f"Bitwise OR of {a} | {b} = {or_result}")
    
    # Bitwise XOR
    xor_result = a ^ b
    print(f"Bitwise XOR of {a} ^ {b} = {xor_result}")
    
    # Bitwise NOT
    not_result_a = ~a
    not_result_b = ~b
    print(f"Bitwise NOT of ~{a} = {not_result_a}")
    print(f"Bitwise NOT of ~{b} = {not_result_b}")
    
    # Left Shift
    left_shift_a = a << 1
    left_shift_b = b << 1
    print(f"Left Shift {a} << 1 = {left_shift_a}")
    print(f"Left Shift {b} << 1 = {left_shift_b}")
    
    # Right Shift
    right_shift_a = a >> 1
    right_shift_b = b >> 1
    print(f"Right Shift {a} >> 1 = {right_shift_a}")
    print(f"Right Shift {b} >> 1 = {right_shift_b}")

# Example usage
a = 12  # 1100 in binary
b = 5   # 0101 in binary

bitwise_operators(a, b)

# Output:
# Bitwise AND of 12 & 5 = 4
# Bitwise OR of 12 | 5 = 13
# Bitwise XOR of 12 ^ 5 = 9
# Bitwise NOT of ~12 = -13
# Bitwise NOT of ~5 = -6
# Left Shift 12 << 1 = 24
# Left Shift 5 << 1 = 10
# Right Shift 12 >> 1 = 6
# Right Shift 5 >> 1 = 2



# Q.4 Write a program to calculate greatest of three numbers.
#Code:
def find_greatest(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

# Example values
a = 7
b = 5
c = 5

# Finding the greatest number
greatest = find_greatest(a, b, c)

print(f"The greatest among {a}, {b}, and {c} is {greatest}")

# Checking conditions
if a == b == c:
    print("All three numbers are equal.")
elif a == b or a == c or b == c:
    print("Two of the numbers are equal.")
else:
    print("All the numbers are different.")

#Output:
#The greatest among 7, 5, and 5 is 7
#Two of the numbers are equal.