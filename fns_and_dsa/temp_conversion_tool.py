#!/usr/bin/env python3

FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    global FAHRENHEIT_TO_CELSIUS_FACTOR
    FAHRENHEIT_TO_CELSIUS_FACTOR = FAHRENHEIT_TO_CELSIUS_FACTOR * (fahrenheit - 32)
    return FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    global CELSIUS_TO_FAHRENHEIT_FACTOR
    CELSIUS_TO_FAHRENHEIT_FACTOR = (CELSIUS_TO_FAHRENHEIT_FACTOR * celsius) + 32
    return CELSIUS_TO_FAHRENHEIT_FACTOR

def user_prompt():
    temp = float(input("Enter the temperature to convert: "))
    pref = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").upper()
    if pref == "C":
        print(f"{temp}°C is {convert_to_fahrenheit(temp)}°F")
    elif pref == "F":
        print(f"{temp}°F is {convert_to_celsius(temp)}°C")
    else:
        print("Please enter F, or C. Other choice is invalid")
        return

user_prompt()