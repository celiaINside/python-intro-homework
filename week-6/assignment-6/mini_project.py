# find_min(numbers) — returns the minimum value (your loop-based implementation, no min())
# find_max(numbers) — returns the maximum value (your loop-based implementation, no max())
# search(numbers, target) — returns the index of target, or -1 if not found
# bubble_sort(numbers) — returns a new sorted list (do not modify the original)
# show_menu() — prints the menu options and returns the user's choice as a string
# main() — the while loop that calls show_menu() and dispatches to the right function

numbers = [42, 17, 83, 5, 61, 29, 74, 8, 55, 93, 31, 66, 14, 47, 78, 3, 59, 22, 86, 40]

def show_menu():
    while True:
        print("=== Number Cruncher ===")
        print("1. Find minimum")
        print("2. Find maximum")
        print("3. Search for a number")
        print("4. Sort the list")
        print("5. Quit")
     
        try:
            user_option = (input("Choose an option (1-5): "))
            if not user_option.isdigit() or not 1 <= int(user_option) <= 5:
                print("Please enter a number from 1 to 5.")
                continue

            return user_option
        except ValueError:
            print("Please enter a number from 1 to 5.")
            continue

def find_min(numbers):
    minimum = numbers[0]     
    for number in numbers:
        if number < minimum:
            minimum = number
    return minimum

def find_max(numbers):
    maximum = numbers[0]
    for number in numbers:
        if number > maximum:
            maximum = number
    return maximum

def search(numbers, target):
    found = False
    index = 0
    for number in numbers:
        if number == target:
            found = True
            break
        index +=1
    if not found:
        return -1
    return index 

def bubble_sort(numbers):
    n = len(numbers)
    sorted_numbers = numbers.copy()
    for i in range(n-1):
        swapped = False
        for j in range(n-i-1):
            if sorted_numbers[j] > sorted_numbers[j+1]:
                sorted_numbers[j], sorted_numbers[j+1] = sorted_numbers[j+1], sorted_numbers[j]
                swapped = True
        if not swapped:  
            break
    return sorted_numbers


# Main menu loop begins. 

def main():
    while True:
        user_option = show_menu()
        if user_option == "1":
            minimum = find_min(numbers)
            print(f"The minimum is {minimum}.")
        elif user_option == "2":
            maximum = find_max(numbers)
            print(f"The maximum is {maximum}.")
        elif user_option == "3":
            try:
                target = int(input("Enter a number: "))
                index = search(numbers, target)
                if index != -1:
                    print(f"Found at index {index}.")
                else:
                    print("Not found.")
            except ValueError:
                print("Please enter a valid number.")
        elif user_option == "4":
            sorted_numbers = bubble_sort(numbers)
            print(f"Sorted: {sorted_numbers}")
        elif user_option == "5":
            print("Goodbye!")
            break
        else:
            print("Please enter a number from 1-5.")

if __name__ == "__main__":
    main()

#this is now show_menu function

#Find minimum — loop through the list and track the smallest value. Do not use Python's built-in min().
    #this is now find_min function

#Find maximum — same approach, tracking the largest value. Do not use max().
    #this is now find_max function

# #Search — ask the user for a number, then implement a linear search loop. Print the index if found, or a "not found" message.
    #this is now search(numbers, target) function

    # found = False
    # index = 0

    # if user_option == 3:
    #     try:
    #         user_number = int(input("Enter a number: "))
    #     except ValueError:
    #             print("Please enter a valid number.")
    #             continue
    #     for number in numbers:
    #             if number == user_number:
    #                 print (f"Found {user_number} at {index}.")
    #                 found = True
    #                 break
    #             index +=1
    #     if not found:
    #             print(f"{user_number} not found.")

# #Sort — implement bubble sort: repeatedly loop through adjacent pairs, swap if out of order, and repeat until no swaps occur. Print the sorted list. Do not use sorted() or .sort().
    #this is now bubble_sort(numbers) function

    # if user_option == 4:
    #     def bubble_sort(numbers):
    #         n = len(numbers)
    #         sorted_numbers = numbers.copy()
    #         for i in range(n-1):
    #             swapped = False
    #             for j in range(n-i-1):
    #                 if sorted_numbers[j] > sorted_numbers[j+1]:
    #                     sorted_numbers[j], sorted_numbers[j+1] = sorted_numbers[j+1], sorted_numbers[j]
    #                     swapped = True
    #             if not swapped:  
    #                 break
    #         return sorted_numbers
    #     print(bubble_sort(numbers))

# #Quit — print a goodbye message and exit the loop.

#     if user_option == 5:
#         print("Goodbye!")
#         break