input1 = input("Enter the numerator: ")
input2 = input("Enter the denominator: ")

try: 
    result = float(input1) / float(input2)
    print(f"{input1} / {input2} = {result:.1f}")
except ValueError:
    print("Please enter only number values.")
except ZeroDivisionError:
    print("Can't divide by zero — please try a non-zero denominator.")