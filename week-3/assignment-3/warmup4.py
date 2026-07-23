user_number = int(input("Enter a number: "))
print (f"Enter a number: {user_number}")

if user_number < 0:
    print (f"{user_number} is negative.")
elif user_number > 0:
    print (f"{user_number} is positive.")
else:
    print (f"{user_number} is zero.")

if user_number % 2 == 0:
    print (f"{user_number} is even.")
elif user_number % 2 != 0:
    print (f"{user_number} is odd.")
else:
    print (f"{user_number} is even.")