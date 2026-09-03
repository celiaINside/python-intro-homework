while True: 
    user_number = input("Enter a number: ")

    try:
        user_number = float(user_number)
        print(f"You entered: {user_number:.1f}")
        break
    
    except ValueError:
        print("That's not a valid number. Try again.")