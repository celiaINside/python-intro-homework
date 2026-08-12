names = ["Mark", "Joy", "Erin", "Marcus"]

user_name = input("Enter a name to search for: ")

found = False
index = 0

for name in names:
    if name.lower() == user_name.lower():
        print (f"Found {name} at {index}.")
        found = True
        break
    index +=1

if not found:
    print(f"{user_name} was not found in the list.")
