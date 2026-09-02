input1 = input("Enter the numerator: ")
input2 = input("Enter the denominator: ")



try: 
    input1 = float(input1)
    input2 = float(input2)
    result = input1 / input2
    print(f"{input1} ÷ {input2} = {result}")
except ValueError:
    print("Can't compute — please enter a valid integer.")
except ZeroDivisionError:
    print("Can't divide by zero — please try a non-zero denominator.")