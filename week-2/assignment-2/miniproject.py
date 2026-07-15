temp_fahr = round(float(input("What is the temperature where you are in Fahrenheit? ")), 1)
celsius = (temp_fahr - 32) * 5 / 9
print (f"{temp_fahr}°F is {celsius:.1f}°C.")