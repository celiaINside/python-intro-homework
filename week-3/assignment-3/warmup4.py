user_number = int(input("Enter a number: "))

if user_number == 0:
    print (f"{user_number} is zero.")
elif user_number < 0:
    print (f"{user_number} is negative.")

if user_number % 2 == 0:
    print (f"{user_number} is even.")
elif user_number % 2 != 0:
    print (f"{user_number} is odd.")