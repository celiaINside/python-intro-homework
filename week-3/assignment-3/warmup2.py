age = int(input("Enter your age: "))
          
print (f"Enter your age: {age}")

if age > 0 and age < 12:
    print ("You are a Child.")
elif age > 12 and age < 18:
    print ("You are a Teen.")
elif age > 18 and age < 65:
    print ("You are an Adult.")
elif score >= 80 and score <= 89:
    print ("Grade: B")
else:
    print ("You are a Senior.")