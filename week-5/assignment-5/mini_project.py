numbers = [42, 17, 83, 5, 61, 29, 74, 8, 55, 93, 31, 66, 14, 47, 78, 3, 59, 22, 86, 40]

while True:
    print("=== Number Cruncher ===")
    print("1. Find minimum")
    print("2. Find maximum")
    print("3. Search for a number")
    print("4. Sort the list")
    print("5. Quit")

    user_option = (int(input("Choose an option (1-5): ")))

#Find minimum — loop through the list and track the smallest value. Do not use Python's built-in min().
    minimum = numbers[0]

    if user_option == 1:
            for number in numbers:
                if number < minimum:
                    minimum = number
            print(f"The minimum is {minimum}.")

#Find maximum — same approach, tracking the largest value. Do not use max().

    maximum = numbers[0]

    if user_option == 2:
            for number in numbers:
                if number > maximum:
                    maximum = number
            print(f"The maximum is {maximum}.")

#Search — ask the user for a number, then implement a linear search loop. Print the index if found, or a "not found" message.

    found = False
    index = 0

    if user_option == 3:
            user_number = int(input("Enter a number: "))
            for number in numbers:
                if number == user_number:
                    print (f"Found {user_number} at {index}.")
                    found = True
                    break
                index +=1

            if not found:
                print(f"{user_number} not found.")

#Sort — implement bubble sort: repeatedly loop through adjacent pairs, swap if out of order, and repeat until no swaps occur. Print the sorted list. Do not use sorted() or .sort().

    n = len(numbers)

    if user_option == 4:
            for i in range(n-1):
                swapped = False
                for j in range(n-i-1):
                    if numbers[j] > numbers[j+1]:
                        numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
                        swapped = True
                if not swapped:  
                    break
            print(numbers)

#Quit — print a goodbye message and exit the loop.

    if user_option == 5:
        print("Goodbye!")
        break