names = ["Mark", "Joy", "Erin", "Marcus"]

user_name = input("Enter a name to search for: ").title()

found = False
index = 0

for name in names:
    if name == user_name:
        print (f"Found {user_name} at {index}.")
        found = True
        break
    index +=1

if not found:
    print(f"{user_name} was not found in the list.")
