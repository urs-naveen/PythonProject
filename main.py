try:
    user_number = int(input("Enter a number: "))
    print(f"You entered: {user_number}")
except ValueError:
    print("Invalid input. Please enter a valid number.")
