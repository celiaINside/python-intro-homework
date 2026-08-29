input1 = input("Enter the numerator: ")
input2 = input("Enter the denominator: ")

input1 = int(input1)
input2 = int(input2)

try: 
    result = (input1) / (input2)
    print(f"{input1} ÷ {input2} = {result:.1f}")
except ZeroDivisionError:
    print("Can't divide by zero — please try a non-zero denominator.")