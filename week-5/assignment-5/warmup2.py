
while True:
    try:
        user_integer = int(input("Enter a positive integer: "))
        if user_integer <= 0:
            print ("That's not a positive integer. Try again.")
        else:
            print (f"Got it: {user_integer}")
            break

    except ValueError:
        print("That's not a positive integer. Try again.")