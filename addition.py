# addition.py
# Accept input from the keyboard
num1 = num2 = 0
try:
    num1 = int(input("Enter first integer: "))
    num2 = int(input("Enter second integer: "))
except ValueError:
    print("Invalid input. Please enter valid integers.")
    exit(1)

# Add the two numbers
result = num1 + num2

# Display the result
print("The sum is:", result)
