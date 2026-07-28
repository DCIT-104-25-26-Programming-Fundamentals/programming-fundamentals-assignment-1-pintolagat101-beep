# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 9
# =============================================================================
#
# TASK: Console-Based Simple Calculator
#
# Build a calculator program that runs in the console and performs basic
# arithmetic operations based on the user's input.
#
# -----------------------------------------------------------------------------
# OPERATIONS YOUR CALCULATOR MUST SUPPORT
# -----------------------------------------------------------------------------
#
#   1. Addition          ( + )    e.g.  10 + 3  =  13
#   2. Subtraction       ( - )    e.g.  10 - 3  =  7
#   3. Multiplication    ( * )    e.g.  10 * 3  =  30
#   4. Division          ( / )    e.g.  10 / 3  =  3.33
#   5. Modulus           ( % )    e.g.  10 % 3  =  1  (remainder)
#   6. Exponentiation    ( ** )   e.g.  2 ** 8  =  256
#   7. Quit
#
# -----------------------------------------------------------------------------
# HOW THE MENU SHOULD LOOK
# -----------------------------------------------------------------------------
#
#   ============================
#        SIMPLE CALCULATOR
#   ============================
#   1. Addition
#   2. Subtraction
#   3. Multiplication
#   4. Division
#   5. Modulus
#   6. Exponentiation
#   7. Quit
#   Select an operation (1-7):
#
# -----------------------------------------------------------------------------
# EXPECTED INTERACTION EXAMPLE
# -----------------------------------------------------------------------------
#
#   Select an operation (1-7): 4
#   Enter first number : 10
#   Enter second number: 3
#   Result: 10 / 3 = 3.33
#
#   Select an operation (1-7): 4
#   Enter first number : 5
#   Enter second number: 0
#   Error: Cannot divide by zero.
#
#   Select an operation (1-7): 7
#   Goodbye!
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Each arithmetic operation MUST be written as its own function.
# - Use a loop so the calculator keeps running until the user selects Quit.
# - Division by zero must be caught and handled with a clear error message
#   (do NOT let the program crash).
# - Division results should be rounded to 2 decimal places.
# - Handle invalid menu choices gracefully.
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================

# Simple Calculator - Assignment 9

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    # need to check for zero or program will crash
    if b == 0:
        print("Error: Cannot divide by zero.")
        return None
    else:
        return round(a / b, 2)

def modulus(a, b):
    if b == 0:
        print("Error: Cannot divide by zero.")
        return None
    else:
        return a % b

def exponent(a, b):
    return a ** b


# main loop starts here
running = True

while running:
    print("")
    print("====================================")
    print("        SIMPLE CALCULATOR")
    print("====================================")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")
    print("6. Exponentiation")
    print("7. Quit")

    choice = input("Select an operation (1-7): ")

    if choice == "7":
        print("Goodbye!")
        running = False

    elif choice == "1":
        num1 = float(input("Enter first number : "))
        num2 = float(input("Enter second number: "))
        result = add(num1, num2)
        print("Result:", result)

    elif choice == "2":
        num1 = float(input("Enter first number : "))
        num2 = float(input("Enter second number: "))
        result = subtract(num1, num2)
        print("Result:", result)

    elif choice == "3":
        num1 = float(input("Enter first number : "))
        num2 = float(input("Enter second number: "))
        result = multiply(num1, num2)
        print("Result:", result)

    elif choice == "4":
        num1 = float(input("Enter first number : "))
        num2 = float(input("Enter second number: "))
        result = divide(num1, num2)
        # only print if it actually worked (not a divide by zero)
        if result != None:
            print("Result:", num1, "/", num2, "=", result)

    elif choice == "5":
        num1 = float(input("Enter first number : "))
        num2 = float(input("Enter second number: "))
        result = modulus(num1, num2)
        if result != None:
            print("Result:", result)

    elif choice == "6":
        num1 = float(input("Enter first number : "))
        num2 = float(input("Enter second number: "))
        result = exponent(num1, num2)
        print("Result:", result)

    else:
        print("Invalid choice, please pick a number between 1 and 7.")
        