from operations import *

def main():
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))

    print(f"Addition: {add(a, b)}")
    print(f"Subtraction: {subtract(a, b)}")
    print(f"Multiplication: {multiply(a, b)}")
    print(f"Division: {divide(a, b)}")

print(main())