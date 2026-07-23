user_number = int(input("Enter a number: "))

if user_number < 0:
    print (f"{user_number} is negative.")
elif user_number > 0:
    print (f"{user_number} is positive.")
elif user_number == 0:
    print (f"{user_number} is zero.")

if user_number % 2 != 0:
    print (f"{user_number} is odd.")
elif user_number % 2 == 0:
    print (f"{user_number} is even.")