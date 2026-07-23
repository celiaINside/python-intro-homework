age = int(input("Enter your age: "))

if age >= 0 and age <= 12:
    print ("You are a Child.")
elif age >= 13 and age <= 17:
    print ("You are a Teen.")
elif age >= 18 and age <= 64:
    print ("You are an Adult.")
elif age >= 80 and age <= 89:
    print ("Grade: B")
else:
    print ("You are a Senior.")