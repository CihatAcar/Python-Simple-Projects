"""
Write a Python program to convert temperatures to and from celsius, fahrenheit.
[ Formula : c/5 = f-32/9 [ where c = temperature in celsius and
 f = temperature in fahrenheit ]
Expected Output :
60°C is 140 in Fahrenheit
45°F is 7 in Celsius
"""


def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 1.8) + 32
    print("The temperature is %d Fahrenheit." % fahrenheit)


def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) / 1.8
    print("The temperature is %d Celsius." % celsius)


temperature = input("Please select which converter do you want to use? Type C for celsius and type F for "
                          "fahrenheit: ")

if temperature == "C":
    C = float(input("Please enter the temperature in Celsius: "))
    celsius_to_fahrenheit(C)
else:
    F = float(input("Please enter the temperature in Celsius: "))
    fahrenheit_to_celsius(F)
