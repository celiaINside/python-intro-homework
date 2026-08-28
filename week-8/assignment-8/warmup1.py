user_number = input("Enter a number: ")

try:
    user_number = float(user_number)
    print(f"You entered: {user_number}")
    
except ValueError:
    print("That's not a valid number. Try again.")