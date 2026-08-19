#Celsius to Fahrenheit function
def celsius_to_fahrenheit(celsius):
    return ((celsius * 9/5) + 32)

def print_celsius_summary(celsius, fahrenheit):
    print(f"{celsius}°C = {fahrenheit:.1f}°F")

#Fahrenheit to Celsius function
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def print_fahrenheit_summary(fahrenheit, celsius):
    print(f"{fahrenheit}°F = {celsius:.1f}°C")


fahrenheit = celsius_to_fahrenheit(0)
print_celsius_summary(0, fahrenheit)

fahrenheit = celsius_to_fahrenheit(100)
print_celsius_summary(100, fahrenheit)

celsius = fahrenheit_to_celsius(72)
print_fahrenheit_summary(72, celsius)

#alternate style of printing results: 

# celsius = 100
# fahrenheit = celsius_to_fahrenheit(celsius)
# print(f"{celsius}°C = {fahrenheit:.1f}°F")